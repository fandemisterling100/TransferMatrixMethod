from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
import json
from app.api.utils import (
    get_range_list,
    order_materials,
    format_graph_data,
    get_dielectric_funtion_from_nk,
    get_values_from_file,
    get_inclusions,
    group_materials,
)
from app.api.transfer_matrix_method import TransferMatrixMethod
from app.api.efective_medium_theories import EfectiveMediumTheories
from app.api.dispersion_models import DispersionModels
from app.api.interpolacion import interpolation
import csv

from app.api.serializers import TransferSerializer


class CalculateDataView(APIView):
    """
    View to receive POST data from the VUE components about the different
    materials and retrieve graphics data
    """

    # Allow requests without CSRF token (to any user on internet)
    permission_classes = [AllowAny]
    # Allow files on post data and input form data
    parser_classes = [MultiPartParser, FormParser]
    # SerializeR for initial parameters
    serializer_class = TransferSerializer

    def post(self, request, *args, **kwargs):
        # Serialize initial parameters to read them as float and not as strings
        serializer = self.serializer_class(data=request.data)
        # Validate that the data recived for initial parameters corresponds to the
        # expected data types (string, float, integer)
        serializer.is_valid(raise_exception=True)
        # Get data as a dic after being serialized
        initial_parameters = serializer.data
        # Transform Querydict into python dict
        data = dict(request.data)
        # Get materials apart from initial parameters
        materials = data.get("materials")
        # Get each initial parameter as an individual variable
        # to call just the name of the variable in the next lines of code
        answer = initial_parameters.get("answer")
        steps = initial_parameters.get("steps")
        polarization = initial_parameters.get("polarization")
        initial_parameter = (
            initial_parameters.get("initialAngle")
            if answer == "angular"
            else initial_parameters.get("initialWaveLength")
        )
        final_parameter = (
            initial_parameters.get("finalAngle")
            if answer == "angular"
            else initial_parameters.get("finalWaveLength")
        )
        fixed_parameter = (
            initial_parameters.get("waveLength")
            if answer == "angular"
            else initial_parameters.get("angle")
        )
        number_of_materials = initial_parameters.get("materialsQuantity")

        # Initialize list to store n,k values
        refractive_indexes = []
        # Initialize thicknesses list
        thicknesses = []

        # Initialize volume list
        volumes = []
        
        # Group materials 
        materials = group_materials(materials)

        # Order materials (Substrate, layers, host)
        materials = order_materials(materials)
        import ipdb; ipdb.set_trace()

        # Iterate over materials to get n, k
        # according to the method selected for each material
        for material in materials:
            if isinstance(material, str):
                material = json.loads(material)
                for material_name in material.keys():
                    material = material.get(material_name)
                    option = material.get("option")

                    # Add layer thickness to the vector
                    if "thickness" in material:
                        thicknesses.append(float(material.get("thickness")))

                    # MANUAL OPTION
                    if option == "manual":
                        n = float(material.get("n"))
                        k = float(material.get("k"))
                        complex_number = complex(n, k)
                        refractive_indexes.append(complex_number)

                    # DIELECTRIC FUNCTION OPTION: LORENZ
                    if option == "lorenz":
                        ne = float(material.get("ne"))
                        wo = float(material.get("wo"))
                        w = float(material.get("w"))
                        r = float(material.get("r"))

                        lorenz_parameters = [ne, wo, w, r]
                        method = DispersionModels(lorenz_parameters)
                        refractive_indexes.append(method.get_lorenz_model())

                    # DIELECTRIC FUNCTION OPTION: DRUDE
                    if option == "drude":
                        ne = float(material.get("ne"))
                        e = float(material.get("e"))
                        w = float(material.get("w"))
                        r = float(material.get("r"))

                        drude_parameters = [ne, e, w, r]
                        method = DispersionModels(drude_parameters)
                        refractive_indexes.append(method.get_drude_model())

                    # DIELECTRIC FUNCTION OPTION: SELLMEIER
                    if option == "sellmeier":
                        a = float(material.get("a"))
                        b = float(material.get("b"))
                        lambda_0 = float(material.get("lambdaO"))
                        lambda_f = float(material.get("lambda"))

                        sellmeier_parameters = [a, b, lambda_f, lambda_0]
                        method = DispersionModels(sellmeier_parameters)
                        refractive_indexes.append(method.get_sellmeier_model())

                    # DIELECTRIC FUNCTION OPTION: CAUCHY
                    if option == "cauchy":
                        a = float(material.get("a"))
                        b = float(material.get("b"))
                        c = float(material.get("c"))
                        lambda_f = float(material.get("lambda"))

                        cauchy_parameters = [a, b, c, lambda_f]
                        method = DispersionModels(cauchy_parameters)
                        refractive_indexes.append(method.get_cauchy_model())

                    # EFFECTIVE MEDIUM THEORIES: MAXWELL
                    if option == "maxwell":
                        # Dielectric
                        if "e" in material:
                            e1m = float(material["e"]["e1m"])
                            e2m = float(material["e"]["e2m"])
                            comp = complex(e1m, e2m)

                        else:
                            nm = float(material["nk"]["nm"])
                            km = float(material["nk"]["km"])
                            comp = get_dielectric_funtion_from_nk(nm, km)

                        inclusions = get_inclusions(material)
                        e_list_inclusions = []
                        for inclusion in inclusions:
                            if inclusion.get("option") == "e":
                                inclusion_e1m = float(inclusion["e1m"])
                                inclusion_e2m = float(inclusion["e2m"])
                                comp_inclusion = complex(inclusion_e1m, inclusion_e2m)
                                e_list_inclusions.append(comp_inclusion)
                            else:
                                inclusion_nm = float(inclusion["nm"])
                                inclusion_km = float(inclusion["km"])
                                comp_inclusion = get_dielectric_funtion_from_nk(
                                    inclusion_nm, inclusion_km
                                )
                                e_list_inclusions.append(comp_inclusion)

                            volume = float(inclusion["volume"])
                            volumes.append(volume)

                        method = EfectiveMediumTheories(
                            epsilon_host_mg=comp,
                            volume_fractions_mg=volumes,
                            epsilon_inclusions_mg=e_list_inclusions,
                        )
                        method_result = method.get_maxwell_garnett()
                        refractive_indexes.append(method_result)
                    
                    # EFFECTIVE MEDIUM THEORIES: LORENTZ
                    if option == "lorentz":
                        # Dielectric
                        eem = material.get('e-em')
                        e1m = eem.get('e1m')
                        e2m = eem.get('e2m')
                        nm = eem.get('nm')
                        km = eem.get('km')
                        
                        eei = material.get('e-ei')
                        e1i = eei.get('e1i')
                        e2i = eei.get('e2i')
                        ni = eei.get('ni')
                        ki = eei.get('ki')
                        volume = float(eei.get('volume'))
                        
                        if e1m or e2m:
                            comp = complex(float(e1m), float(e2m))
                        elif nm or km:
                            comp = get_dielectric_funtion_from_nk(float(nm), float(km))
                            
                        
                        if e1i or e2i:
                            comp_inclusion = complex(float(e1i), float(e2i))
                        elif ni or ki:
                            comp_inclusion = get_dielectric_funtion_from_nk(float(ni), float(ki))
                            
                        method = EfectiveMediumTheories(
                            epsilon_host_ll=comp, 
                            volume_fractions_ll=volume,
                            epsilon_inclusion_ll=comp_inclusion,
                        )
                        method_result = method.get_lorentz_lorenz()
                        refractive_indexes.append(method_result)
                         
            # Reading an InMemoryFile
            else:
                # Get extension
                file_type = material.content_type.split("/")[1]

                # Read file
                decoded_file = material.read().decode("utf-8").splitlines()

                # Set initial parameters
                w_i = (
                    initial_parameters.get("waveLength")
                    if answer == "angular"
                    else initial_parameters.get("initialWaveLength")
                )
                w_f = (
                    w_i
                    if answer == "angular"
                    else initial_parameters.get("finalWaveLength")
                )

                # Get list of values for wl, n and k
                wl_list, n_list, k_list = get_values_from_file(decoded_file, file_type)

                # Calculate interpolation
                result = interpolation(
                    (wl_list, n_list, k_list), w_i, w_f, steps, respuesta=answer
                )
                if 'maxwell' in material.name:
                    comp = get_dielectric_funtion_from_nk(result.real, result.imag)
                    method = EfectiveMediumTheories(
                        epsilon_host_mg=comp,
                    )
                    result = method.get_maxwell_garnett()
                    
                print("INTERPOLACION---------------------", result)
                # Add n,k to the refractive indexes list
                if answer == "angular":
                    refractive_indexes.append(result)
                else:
                    refractive_indexes += result

        # Get values for 'x' axis
        x_range = get_range_list(initial_parameter, final_parameter, steps)
        print(x_range)

        # Initialize final §§c
        reflectances = []
        transmittances = []
        absortances = []

        # Calculate 'y' axis values using Transfer Matrix Method
        if answer == "angular":
            for x in x_range:
                method = TransferMatrixMethod(
                    theta=x,
                    l=fixed_parameter,
                    n=refractive_indexes,
                    thicknesses=thicknesses,
                    polarization=polarization.upper(),
                )
                reflectance = method.get_reflectance()
                reflectances.append(reflectance)

                transmittance = method.get_transmittance()
                transmittances.append(transmittance)

                absortance = method.get_absortance()
                absortances.append(absortance)

        # Format data to be just real numbers of float type with 2 decimal places
        graph_data = {
            "reflectance": format_graph_data(reflectances),
            "transmittance": format_graph_data(transmittances),
            "absortances": format_graph_data(absortances),
            "x_range": format_graph_data(x_range),
        }
        print(data)
        # Return a response with the graphics data and a confirmation to the browser about
        # the correct result of the POST request
        print(graph_data)
        return Response(graph_data, status=status.HTTP_200_OK)

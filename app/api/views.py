from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
import json
from app.api.utils import get_range_list, format_graph_data
from app.api.transfer_matrix_method import TransferMatrixMethod

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

        # Iterate over materials to get n, k
        # according to the method selected for each material
        for material in materials:
            material = json.loads(material)
            for material_name in material.keys():
                material = material.get(material_name)
                option = material.get("option")
                
                # MANUAL OPTION
                if option == "manual":
                    n = float(material.get("n"))
                    k = float(material.get("k"))
                    complex_number = complex(n, k)
                    refractive_indexes.append(complex_number)

                if option == "file":
                    pass

                if option == "dielectric":
                    pass
        
        # Get values for 'x' axis
        x_range = get_range_list(initial_parameter, final_parameter, steps)
        
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
                
                transmittance =method.get_transmittance()
                transmittances.append(transmittance)
            
                absortance = method.get_absortance()
                absortances.append(absortance)

        # Format data to be just real numbers of float type with 2 decimal places
        graph_data = {
            'reflectance': format_graph_data(reflectances),
            'transmittance': format_graph_data(transmittances),
            'absortances': format_graph_data(absortances),
            'x_range': format_graph_data(x_range),
        }
        print(data)
        # Return a response with the graphics data and a confirmation to the browser about
        # the correct result of the POST request
        print(graph_data)
        return Response(graph_data, status=status.HTTP_200_OK)

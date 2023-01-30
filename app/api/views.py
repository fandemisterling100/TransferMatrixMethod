from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser


from app.api.serializers import (
    UserSerializer,
    TransferSerializer,
)

User = get_user_model()


class UserViewSet(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class CalculateDataView(APIView):
    # Allow requests withoud CSRF token
    permission_classes = [AllowAny]
    # Allow files on post data
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = TransferSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        initial_parameters = serializer.data
        materials = request.data.get('materials')
        answer = initial_parameters.get("answer")
        steps = initial_parameters.get("steps")
        polarization = initial_parameters.get("polarization") 
        initial_parameter = initial_parameters.get("initialAngle") if answer == 'angular ' else initial_parameters.get("initialWaveLength")
        final_parameter = initial_parameters.get("finalAngle") if answer == 'angular ' else initial_parameters.get("finalWaveLength") 
        fixed_parameter = initial_parameters.get("waveLength") if answer == 'angular ' else initial_parameters.get("angle") 
        number_of_materials = initial_parameters.get("materialsQuantity") 
        import ipdb; ipdb.set_trace()

        if answer == "angular": 
            #materials = get_data_from_file(file)
            materials = []
            for i in range(0, materials):
                list_n = []
                list_k = []
                if i == "file":
                    file_name = ""

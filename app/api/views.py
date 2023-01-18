from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from app.api.serializers import (
    UserSerializer,
)

User = get_user_model()


class UserViewSet(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()

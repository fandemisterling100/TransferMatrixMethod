from rest_framework import serializers
from app.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "name"]

class TransferSerializer(serializers.Serializer):
    initialAngle = serializers.FloatField(required=False)
    finalAngle = serializers.FloatField(required=False)
    angle = serializers.FloatField(required=False)
    steps = serializers.IntegerField(required=False)
    initialWaveLength = serializers.FloatField(required=False)
    finalWaveLength = serializers.FloatField(required=False)
    waveLength = serializers.FloatField(required=False)
    polarization = serializers.CharField(required=False)
    substrate = serializers.CharField(required=False)
    host = serializers.CharField(required=False)
    materialsQuantity = serializers.IntegerField(required=False)
    answer = serializers.CharField(required=False)
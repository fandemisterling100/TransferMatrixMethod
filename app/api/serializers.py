from rest_framework import serializers
from app.users.models import User


class TransferSerializer(serializers.Serializer):
    """
    Serializer for initial parameters. Each parameters has its own
    data type:

    CharField = String
    IntegerField = Integer
    FloatField = Float

    None of the parameters is required to avoid errors with
    the request but still all of them can be received
    """

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

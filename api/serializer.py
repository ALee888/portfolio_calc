from rest_framework import serializers

class CalculationSerializer(serializers.Serializer):
    name = serializers.CharField()
    total = serializers.FloatField()

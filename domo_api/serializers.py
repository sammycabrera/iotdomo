from rest_framework import serializers

class LocationSerializer(serializers.Serializer):
    name_location = serializers.CharField(max_length=255)
    user_id = serializers.IntegerField()

class DeviceSerializer(serializers.Serializer):
    name_device=serializers.CharField(max_length=255)
    unidad=serializers.CharField(max_length=255)
    location_id=serializers.IntegerField()

class DotSerializer(serializers.Serializer):
    value=serializers.FloatField()
    datTime=serializers.DateTimeField()
    device_id=serializers.IntegerField()
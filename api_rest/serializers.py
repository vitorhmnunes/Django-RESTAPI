from rest_framework import serializers

from api_rest import models

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = '__all__'

class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rent
        fields = '__all__'
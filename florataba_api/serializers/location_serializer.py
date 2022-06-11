from rest_framework import serializers

from florataba_api.models.location import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

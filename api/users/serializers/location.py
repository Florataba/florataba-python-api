from rest_framework import serializers

from domain.users.models import Location


class LocationOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class LocationUpdateSerializer(serializers.Serializer):
    street = serializers.CharField(max_length=64, required=False, allow_blank=True)
    region = serializers.CharField(max_length=32, required=False, allow_blank=True)
    build_number = serializers.CharField(max_length=10, required=False, allow_blank=False)
    apartment_number = serializers.CharField(max_length=10, required=False, allow_blank=False)


class LocationInputSerializer(serializers.Serializer):
    street = serializers.CharField(max_length=64, required=False, allow_blank=True)
    region = serializers.CharField(max_length=32, required=False, allow_blank=True)
    build_number = serializers.CharField(max_length=10, required=True, allow_blank=False)
    apartment_number = serializers.CharField(max_length=10, required=True, allow_blank=False)

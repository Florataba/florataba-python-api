from rest_framework import serializers

from domain.orders.models import Bouquet


class BouquetOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bouquet
        fields = "__all__"


class BouquetUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=32, required=False, allow_blank=False)
    event_type_bouquet = serializers.CharField(max_length=36, required=False, allow_blank=False)
    description = serializers.CharField(max_length=1000, required=False, allow_blank=False)
    price = serializers.DecimalField(max_digits=5, decimal_places=2, required=False, allow_null=False)
    is_single_bouquet = serializers.BooleanField(required=False)
    available_quantity = serializers.IntegerField(required=False)
    img_url = serializers.CharField(max_length=255, required=False, allow_null=False)


class BouquetInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=32, required=True, allow_blank=False)
    event_type_bouquet = serializers.CharField(max_length=36, required=False, allow_blank=False)
    description = serializers.CharField(max_length=1000, required=True, allow_blank=False)
    price = serializers.DecimalField(max_digits=5, decimal_places=2, required=False, allow_null=False)
    is_single_bouquet = serializers.BooleanField(required=False)
    available_quantity = serializers.IntegerField(required=True)
    img_url = serializers.CharField(max_length=255, allow_null=False)

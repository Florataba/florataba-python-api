from rest_framework import serializers

from domain.orders.models import OrderDetails


class OrderDetailsOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = "__all__"


class OrderDetailsUpdateSerializer(serializers.Serializer):
    order_info = serializers.CharField(max_length=255, required=False, allow_blank=False)
    address_id = serializers.UUIDField(required=False, allow_null=False)
    total_price = serializers.DecimalField(max_digits=9, decimal_places=2, required=False, allow_null=False)


class OrderDetailsInputSerializer(serializers.Serializer):
    order_info = serializers.CharField(max_length=255, required=True, allow_blank=False)
    address_id = serializers.UUIDField(required=True, allow_null=False)
    total_price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True, allow_null=False)

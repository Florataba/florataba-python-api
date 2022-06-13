from rest_framework import serializers

from api.orders.serializers import OrderDetailsOutputSerializer
from domain.orders.models import Order


class OrderOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "status",
            "order_details"
        )

        order_details = serializers.SerializerMethodField()

        @classmethod
        def get_order_details(cls, obj: Order) -> dict:
            if obj.order_details:
                return OrderDetailsOutputSerializer(obj.order_details).data
            else:
                return {}


class OrderUpdateSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=50, required=True, allow_null=False)


class OrderInputSerializer(OrderUpdateSerializer):
    order_details_id = serializers.UUIDField(required=True)

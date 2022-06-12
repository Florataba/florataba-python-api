from rest_framework import serializers

from domain.models.orders import OrderDetails


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'

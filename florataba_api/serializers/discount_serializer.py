from rest_framework import serializers

from florataba_api.models.discount import Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

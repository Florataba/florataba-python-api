from rest_framework import serializers

from domain.users.models import Discount


class DiscountOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"


class DiscountUpdateSerializer(serializers.Serializer):
    type = serializers.IntegerField(required=False)
    benefits_text = serializers.CharField(max_length=255, required=False, allow_blank=False)
    discount_percent = serializers.DecimalField(max_digits=5, decimal_places=2, required=False, allow_null=False)


class DiscountInputSerializer(serializers.Serializer):
    type = serializers.IntegerField(required=True)
    benefits_text = serializers.CharField(max_length=255, required=True, allow_blank=False)
    discount_percent = serializers.DecimalField(max_digits=5, decimal_places=2, required=True, allow_null=False)

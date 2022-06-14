from rest_framework import serializers

from domain.orders.models import Payment


class PaymentOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = (
            "cvv",
        )


class PaymentUpdateSerializer(serializers.Serializer):
    card_number = serializers.CharField(max_length=16, required=False, allow_blank=False)
    user_id = serializers.UUIDField(required=False)
    cvv = serializers.CharField(max_length=3, required=False, allow_blank=False)
    placeholder_name = serializers.CharField(max_length=80, allow_blank=True, required=False)
    bank_name = serializers.CharField(max_length=20, required=False, allow_blank=False)
    expiration_date = serializers.DateField(required=False)


class PaymentInputSerializer(serializers.Serializer):
    card_number = serializers.CharField(max_length=16, required=True, allow_blank=False)
    user_id = serializers.UUIDField(required=True)
    cvv = serializers.CharField(max_length=3, required=True, allow_blank=False)
    placeholder_name = serializers.CharField(max_length=80, allow_blank=True, required=False)
    bank_name = serializers.CharField(max_length=20, required=True, allow_blank=False)
    expiration_date = serializers.DateField(required=True)

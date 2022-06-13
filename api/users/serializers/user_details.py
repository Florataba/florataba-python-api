from rest_framework import serializers

from domain.users.models import UserDetails


class UserDetailsOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = "__all__"


class UserDetailsUpdateSerializer(serializers.Serializer):
    discount_id = serializers.UUIDField(required=False)
    delivery_address_id = serializers.UUIDField(required=False)


class UserDetailsInputSerializer(serializers.Serializer):
    discount_id = serializers.UUIDField(required=True)
    delivery_address_id = serializers.UUIDField(required=True)

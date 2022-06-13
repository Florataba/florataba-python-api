from rest_framework import serializers

from api.users.serializers import UserDetailsOutputSerializer
from domain.users.models import User


class UserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "surname",
            "email",
            "phone_number",
            "details_id"
        )

        details_id = serializers.SerializerMethodField()

        @classmethod
        def get_details_id(cls, obj: User) -> dict:
            if obj.details_id:
                return UserDetailsOutputSerializer(obj.details_id).data
            else:
                return {}


class UserUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    surname = serializers.CharField(max_length=30, required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=False)
    phone_number = serializers.CharField(max_length=20, required=False, allow_blank=False)
    details_id = serializers.UUIDField(required=False)
    password = serializers.CharField(max_length=64, required=False, allow_blank=False)


class UserInputSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    surname = serializers.CharField(max_length=30, required=False, allow_blank=True)
    email = serializers.EmailField(required=True, allow_blank=False)
    phone_number = serializers.CharField(max_length=20, required=True, allow_blank=False)
    details_id = serializers.UUIDField(required=False)
    password = serializers.CharField(max_length=64, required=True, allow_blank=False)

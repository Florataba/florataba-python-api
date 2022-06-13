from rest_framework import serializers

from domain.internal.models import Notification


class NotificationOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class NotificationUpdateSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=50, required=False, allow_blank=False)
    text = serializers.CharField(max_length=255, required=False, allow_blank=False)


class NotificationInputSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=50, required=True, allow_blank=False)
    text = serializers.CharField(max_length=255, required=True, allow_blank=False)

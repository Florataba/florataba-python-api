from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)


from domain.models.users import Notification
from api.serializers.notification_serializer import NotificationSerializer


class NotificationListCreateAPIView(ListCreateAPIView):
    serializer_class = Notification
    queryset = Notification.objects.all()


class NotificationRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

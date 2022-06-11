from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)


from florataba_api.models.order import Order
from florataba_api.serializers.order_serializer import OrderSerializer


class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)


from florataba_api.models.order_details import OrderDetails
from florataba_api.serializers.order_details_serializer import OrderDetailsSerializer


class OrderDetailsListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderDetailsSerializer
    queryset = OrderDetails.objects.all()


class OrderDetailsRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailsSerializer
    queryset = OrderDetails.objects.all()

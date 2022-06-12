from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)


from domain.models.users import Discount
from api.serializers.discount_serializer import DiscountSerializer


class DiscountListCreateAPIView(ListCreateAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()


class DiscountRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()

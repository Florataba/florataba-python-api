from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)


from domain.models.orders import Bouquet
from api.serializers.bouquet_serializer import BouquetSerializer


class BouquetListCreateAPIView(ListCreateAPIView):
    serializer_class = BouquetSerializer
    queryset = Bouquet.objects.all()


class BouquetRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BouquetSerializer
    queryset = Bouquet.objects.all()

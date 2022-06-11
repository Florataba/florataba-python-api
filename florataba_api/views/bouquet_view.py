from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)


from florataba_api.models.bouquet import Bouquet
from florataba_api.serializers.bouquet_serializer import BouquetSerializer


class BouquetListCreateAPIView(ListCreateAPIView):
    serializer_class = BouquetSerializer
    queryset = Bouquet.objects.all()


class BouquetRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BouquetSerializer
    queryset = Bouquet.objects.all()

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)


from domain.models.users import Location
from api.serializers.location_serializer import LocationSerializer


class LocationListCreateAPIView(ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)


from florataba_api.models.location import Location
from florataba_api.serializers.location_serializer import LocationSerializer


class LocationListCreateAPIView(ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)


from florataba_api.models.user_details import UserDetails
from florataba_api.serializers.user_details_serializer import UserDetailsSerializer


class UserDetailsListCreateAPIView(ListCreateAPIView):
    serializer_class = UserDetailsSerializer
    queryset = UserDetails.objects.all()


class UserDetailsRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailsSerializer
    queryset = UserDetails.objects.all()

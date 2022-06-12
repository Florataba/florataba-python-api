from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)


from domain.models.users import UserDetails
from api.serializers.user_details_serializer import UserDetailsSerializer


class UserDetailsListCreateAPIView(ListCreateAPIView):
    serializer_class = UserDetailsSerializer
    queryset = UserDetails.objects.all()


class UserDetailsRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailsSerializer
    queryset = UserDetails.objects.all()

from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)

from florataba_api.models.payment import Payment
from florataba_api.models.user import Document, User
from florataba_api.serializers.payment_serializer import PaymentSerializer
from florataba_api.serializers.user_serializer import DocumentSerializer, UserSerializer
from rest_framework.response import Response


class PaymentListCreateAPIView(ListCreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        created_response = super().create(request, *args, **kwargs)
        if created_response.data.get("placeholder_name") is None:
            request_serializer = self.get_serializer(data=request_data)
            request_serializer.is_valid(raise_exception=True)
            request_obj = request_serializer.save()
            user_id = int(request_data.pop('user')[0])
            print(user_id)
            user_obj = User.objects.get(id=user_id)
            request_obj.set_placeholder_name(user_obj)  # INTERFACE INJECTION
            request_obj.set_card_owner(user_obj)  # INTERFACE INJECTION
            request_obj.save()
            return Response(request_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return created_response


class PaymentRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

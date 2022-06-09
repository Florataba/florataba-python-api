from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)


from florataba_api.models.user import Document, User
from florataba_api.serializers.user_serializer import DocumentSerializer, UserSerializer


class DocumentListCreateAPIView(ListCreateAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    # def create(self, request, *args, **kwargs):
    #     request_data = request.data.copy()
    #     request_serializer = self.get_serializer(data=request_data)
    #     request_serializer.is_valid(raise_exception=True)
    #     request_obj = request_serializer.save()
    #     user_id = int(request_data.pop('user')[0])
    #     request_obj.user = User.objects.get(id=user_id)  # PROPERTY INJECTION
    #     request_obj.save()
    #     return Response(request_serializer.data, status=status.HTTP_201_CREATED)


class DocumentRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


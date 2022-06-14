from django.core.exceptions import ValidationError
from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
)
from injector import inject
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView

from api.users.serializers import (
    UserLoginSerializer,
    UserOutputSerializer,
)
from app_services.users import UserService
from domain.core.exceptions import CredentialsNotValidError


class UserLoginAPIView(APIView):
    """API to login a user."""
    GROUP_TAG = ["auth"]

    def __init__(self, user_service: UserService = UserService(), *args, **kwargs):
        super(UserLoginAPIView, self).__init__(**kwargs)
        self.service = user_service

    def dispatch(self, request, *args, **kwargs):
        return super(UserLoginAPIView, self).dispatch(request, *args, **kwargs)

    @inject
    def setup(self, request, csv_loader_service: UserService = UserService(), *args, **kwargs):
        super(UserLoginAPIView, self).setup(request, csv_loader_service, args, kwargs)

    @extend_schema(
        request=UserLoginSerializer,
        responses={
            200: OpenApiResponse(response=UserOutputSerializer),
        },
        tags=GROUP_TAG,
    )
    def post(self, request):
        incoming_data = UserLoginSerializer(data=request.data)
        incoming_data.is_valid(raise_exception=True)

        try:
            user = UserService().login(incoming_data.validated_data)

            output_serializer = UserOutputSerializer(user)
            return Response(
                output_serializer.data, status=HTTP_200_OK
            )
        except (CredentialsNotValidError, ValidationError) as e:
            return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)

from django.core.exceptions import ValidationError
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiParameter,
)
from injector import inject
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_409_CONFLICT,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.viewsets import ViewSet

from api.users.serializers import (
    UserDetailsOutputSerializer,
    UserDetailsInputSerializer,
    UserDetailsUpdateSerializer,
)
from app_services.users import UserDetailsService
from domain.core.exceptions import (
    ObjectDoesNotExistError,
    ObjectCannotBeDeletedError,
)


class UserDetailsViewSet(ViewSet):
    GROUP_TAG = ["user_details"]

    """
    User Details view.
    """

    def __init__(
            self, service: UserDetailsService = UserDetailsService(),
            **kwargs
    ):
        super(UserDetailsViewSet, self).__init__(**kwargs)
        self.service = service

    def dispatch(self, request, *args, **kwargs):
        return super(UserDetailsViewSet, self).dispatch(request, *args, **kwargs)

    @inject
    def setup(
            self, request, service: UserDetailsService = UserDetailsService(),
            *args, **kwargs
    ):
        super(UserDetailsViewSet, self).setup(request, service, args, kwargs)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=None,
        responses={
            200: OpenApiResponse(response=UserDetailsOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
        },
        tags=GROUP_TAG
    )
    def retrieve(self, request, pk):
        """
        Get User Details.
        """
        try:
            user_details = self.service.get_by_id(pk)

            output_serializer = UserDetailsOutputSerializer(user_details)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)

    @extend_schema(
        request=None,
        responses={
            200: OpenApiResponse(response=UserDetailsOutputSerializer(many=True)),
            400: OpenApiResponse(description="Bad request"),
        },
        tags=GROUP_TAG
    )
    def list(self, request):
        """
        Get all User Details.
        """
        user_detailss = self.service.get_all()

        output_serializer = UserDetailsOutputSerializer(user_detailss, many=True)
        return Response(output_serializer.data, status=HTTP_200_OK)

    @extend_schema(
        parameters=None,
        request=UserDetailsInputSerializer,
        responses={
            201: OpenApiResponse(response=UserDetailsOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
        },
        tags=GROUP_TAG
    )
    def create(self, request):
        """
        Create User Details.
        """
        incoming_data = UserDetailsInputSerializer(data=request.data)
        incoming_data.is_valid(raise_exception=True)

        try:
            user_details = self.service.create(incoming_data.validated_data)

            output_serializer = UserDetailsOutputSerializer(user_details)
            return Response(output_serializer.data, status=HTTP_201_CREATED)
        except (ObjectDoesNotExistError, ValidationError) as e:
            return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=UserDetailsUpdateSerializer,
        responses={
            200: OpenApiResponse(response=UserDetailsOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
        },
        tags=GROUP_TAG
    )
    def update(self, request, pk):
        """
        Update User Details.
        """
        incoming_data = UserDetailsUpdateSerializer(data=request.data)
        incoming_data.is_valid(raise_exception=True)

        try:
            user_details = self.service.update(pk, incoming_data.validated_data)

            output_serializer = UserDetailsOutputSerializer(user_details)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=None,
        responses={
            200: OpenApiResponse(response=UserDetailsOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
            409: OpenApiResponse(description="Resource cannot be deleted: it has linked data")
        },
        tags=GROUP_TAG
    )
    def destroy(self, request, pk):
        """
        Delete User Details.
        """
        try:
            deleted_user_details = self.service.delete(pk)

            output_serializer = UserDetailsOutputSerializer(deleted_user_details)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
        except ObjectCannotBeDeletedError as e:
            return Response({"message": e.message}, status=HTTP_409_CONFLICT)

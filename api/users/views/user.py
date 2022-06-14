from django.core.exceptions import ValidationError
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiParameter,
)
from injector import inject
from rest_framework.decorators import action
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
    UserOutputSerializer,
    UserInputSerializer,
    UserUpdateSerializer,
)
from app_services.users import UserService
from domain.core.exceptions import (
    ObjectDoesNotExistError,
    ObjectCannotBeDeletedError,
)


class UserViewSet(ViewSet):
    GROUP_TAG = ["users"]

    """
    User view.
    """

    def __init__(
            self, service: UserService = UserService(),
            **kwargs
    ):
        super(UserViewSet, self).__init__(**kwargs)
        self.service = service

    def dispatch(self, request, *args, **kwargs):
        return super(UserViewSet, self).dispatch(request, *args, **kwargs)

    @inject
    def setup(
            self, request, service: UserService = UserService(),
            *args, **kwargs
    ):
        super(UserViewSet, self).setup(request, service, args, kwargs)

    @extend_schema(
        parameters=[OpenApiParameter("email", OpenApiTypes.EMAIL, OpenApiParameter.QUERY, required=True)],
        request=UserUpdateSerializer,
        responses={
            200: OpenApiResponse(response=UserOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
            409: OpenApiResponse(description="Resource cannot be deleted: it has linked data")
        },
        tags=GROUP_TAG
    )
    @action(methods=["get", "put", "delete"], detail=False, url_path="by-email")
    def retrieve_by_email(self, request):
        """
        Get/Update/Delete User.
        """
        if request.method == "GET":
            try:
                user = self.service.get_by_id(request.query_params.get("email"))

                output_serializer = UserOutputSerializer(user)
                return Response(output_serializer.data, status=HTTP_200_OK)
            except ObjectDoesNotExistError as e:
                return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)

        if request.method == "PUT":
            incoming_data = UserUpdateSerializer(data=request.data)
            incoming_data.is_valid(raise_exception=True)

            try:
                user = self.service.update(
                    request.query_params.get("email"), incoming_data.validated_data
                )

                output_serializer = UserOutputSerializer(user)
                return Response(output_serializer.data, status=HTTP_200_OK)
            except ObjectDoesNotExistError as e:
                return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
            except ValidationError as e:
                return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)

        if request.method == "DELETE":
            try:
                deleted_user = self.service.delete(request.query_params.get("email"))

                output_serializer = UserOutputSerializer(deleted_user)
                return Response(output_serializer.data, status=HTTP_200_OK)
            except ObjectDoesNotExistError as e:
                return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
            except ObjectCannotBeDeletedError as e:
                return Response({"message": e.message}, status=HTTP_409_CONFLICT)

    @extend_schema(
        request=None,
        responses={
            200: OpenApiResponse(response=UserOutputSerializer(many=True)),
            400: OpenApiResponse(description="Bad request"),
        },
        tags=GROUP_TAG
    )
    def list(self, request):
        """
        Get all Users.
        """
        users = self.service.get_all()

        output_serializer = UserOutputSerializer(users, many=True)
        return Response(output_serializer.data, status=HTTP_200_OK)

    @extend_schema(
        parameters=None,
        request=UserInputSerializer,
        responses={
            201: OpenApiResponse(response=UserOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
        },
        tags=GROUP_TAG
    )
    def create(self, request):
        """
        Create User.
        """
        incoming_data = UserInputSerializer(data=request.data)
        incoming_data.is_valid(raise_exception=True)

        try:
            user = self.service.create(incoming_data.validated_data)

            output_serializer = UserOutputSerializer(user)
            return Response(output_serializer.data, status=HTTP_201_CREATED)
        except (ObjectDoesNotExistError, ValidationError) as e:
            return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)

    # @extend_schema(
    #     parameters=[OpenApiParameter("email", OpenApiTypes.EMAIL, OpenApiParameter.QUERY, required=True)],
    #     request=UserUpdateSerializer,
    #     responses={
    #         200: OpenApiResponse(response=UserOutputSerializer),
    #         400: OpenApiResponse(description="Bad request"),
    #         404: OpenApiResponse(description="Resource not found"),
    #     },
    #     tags=GROUP_TAG
    # )
    # @action(methods=["put"], detail=False)
    # def update_by_email(self, request):
    #     """
    #     Update User.
    #     """
    #     incoming_data = UserUpdateSerializer(data=request.data)
    #     incoming_data.is_valid(raise_exception=True)
    #
    #     try:
    #         user = self.service.update(
    #             request.query_params.get("email"), incoming_data.validated_data
    #         )
    #
    #         output_serializer = UserOutputSerializer(user)
    #         return Response(output_serializer.data, status=HTTP_200_OK)
    #     except ObjectDoesNotExistError as e:
    #         return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
    #     except ValidationError as e:
    #         return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)
    #
    # @extend_schema(
    #     parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
    #     request=None,
    #     responses={
    #         200: OpenApiResponse(response=UserOutputSerializer),
    #         400: OpenApiResponse(description="Bad request"),
    #         404: OpenApiResponse(description="Resource not found"),
    #         409: OpenApiResponse(description="Resource cannot be deleted: it has linked data")
    #     },
    #     tags=GROUP_TAG
    # )
    # def destroy(self, request, pk):
    #     """
    #     Delete User.
    #     """
    #     try:
    #         deleted_user = self.service.delete(pk)
    #
    #         output_serializer = UserOutputSerializer(deleted_user)
    #         return Response(output_serializer.data, status=HTTP_200_OK)
    #     except ObjectDoesNotExistError as e:
    #         return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
    #     except ObjectCannotBeDeletedError as e:
    #         return Response({"message": e.message}, status=HTTP_409_CONFLICT)

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
    LocationOutputSerializer,
    LocationInputSerializer,
    LocationUpdateSerializer,
)
from app_services.users import LocationService
from domain.core.exceptions import (
    ObjectDoesNotExistError,
    ObjectCannotBeDeletedError,
)


class LocationViewSet(ViewSet):
    GROUP_TAG = ["locations"]

    """
    Location view.
    """

    def __init__(
            self, service: LocationService = LocationService(),
            **kwargs
    ):
        super(LocationViewSet, self).__init__(**kwargs)
        self.service = service

    def dispatch(self, request, *args, **kwargs):
        return super(LocationViewSet, self).dispatch(request, *args, **kwargs)

    @inject
    def setup(
            self, request, service: LocationService = LocationService(),
            *args, **kwargs
    ):
        super(LocationViewSet, self).setup(request, service, args, kwargs)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=None,
        responses={
            200: OpenApiResponse(response=LocationOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
        },
        tags=GROUP_TAG
    )
    def retrieve(self, request, pk):
        """
        Get Location.
        """
        try:
            location = self.service.get_by_id(pk)

            output_serializer = LocationOutputSerializer(location)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)

    @extend_schema(
        request=None,
        responses={
            200: OpenApiResponse(response=LocationOutputSerializer(many=True)),
            400: OpenApiResponse(description="Bad request"),
        },
        tags=GROUP_TAG
    )
    def list(self, request):
        """
        Get all Locations.
        """
        locations = self.service.get_all()

        output_serializer = LocationOutputSerializer(locations, many=True)
        return Response(output_serializer.data, status=HTTP_200_OK)

    @extend_schema(
        parameters=None,
        request=LocationInputSerializer,
        responses={
            201: OpenApiResponse(response=LocationOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
        },
        tags=GROUP_TAG
    )
    def create(self, request):
        """
        Create Location.
        """
        incoming_data = LocationInputSerializer(data=request.data)
        incoming_data.is_valid(raise_exception=True)

        try:
            location = self.service.create(incoming_data.validated_data)

            output_serializer = LocationOutputSerializer(location)
            return Response(output_serializer.data, status=HTTP_201_CREATED)
        except (ObjectDoesNotExistError, ValidationError) as e:
            return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=LocationUpdateSerializer,
        responses={
            200: OpenApiResponse(response=LocationOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
        },
        tags=GROUP_TAG
    )
    def update(self, request, pk):
        """
        Update Location.
        """
        incoming_data = LocationUpdateSerializer(data=request.data)
        incoming_data.is_valid(raise_exception=True)

        try:
            location = self.service.update(pk, incoming_data.validated_data)

            output_serializer = LocationOutputSerializer(location)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=None,
        responses={
            200: OpenApiResponse(response=LocationOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
            409: OpenApiResponse(description="Resource cannot be deleted: it has linked data")
        },
        tags=GROUP_TAG
    )
    def destroy(self, request, pk):
        """
        Delete Location.
        """
        try:
            deleted_location = self.service.delete(pk)

            output_serializer = LocationOutputSerializer(deleted_location)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
        except ObjectCannotBeDeletedError as e:
            return Response({"message": e.message}, status=HTTP_409_CONFLICT)

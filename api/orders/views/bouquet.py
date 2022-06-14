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

from api.orders.serializers import (
    BouquetOutputSerializer,
    BouquetInputSerializer,
    BouquetUpdateSerializer,
)
from app_services.orders import BouquetService
from domain.core.exceptions import (
    ObjectDoesNotExistError,
    ObjectCannotBeDeletedError,
)


class BouquetViewSet(ViewSet):
    GROUP_TAG = ["bouquets"]

    """
    Bouquet view.
    """

    def __init__(
            self, service: BouquetService = BouquetService(),
            **kwargs
    ):
        super(BouquetViewSet, self).__init__(**kwargs)
        self.service = service

    def dispatch(self, request, *args, **kwargs):
        return super(BouquetViewSet, self).dispatch(request, *args, **kwargs)

    @inject
    def setup(
            self, request, service: BouquetService = BouquetService(),
            *args, **kwargs
    ):
        super(BouquetViewSet, self).setup(request, service, args, kwargs)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=None,
        responses={
            200: OpenApiResponse(response=BouquetOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
        },
        tags=GROUP_TAG
    )
    def retrieve(self, request, pk):
        """
        Get Bouquet.
        """
        try:
            bouquet = self.service.get_by_id(pk)

            output_serializer = BouquetOutputSerializer(bouquet)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)

    @extend_schema(
        request=None,
        responses={
            200: OpenApiResponse(response=BouquetOutputSerializer(many=True)),
            400: OpenApiResponse(description="Bad request"),
        },
        tags=GROUP_TAG
    )
    def list(self, request):
        """
        Get all Bouquets.
        """
        bouquets = self.service.get_all()

        output_serializer = BouquetOutputSerializer(bouquets, many=True)
        return Response(output_serializer.data, status=HTTP_200_OK)

    @extend_schema(
        parameters=None,
        request=BouquetInputSerializer,
        responses={
            201: OpenApiResponse(response=BouquetOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
        },
        tags=GROUP_TAG
    )
    def create(self, request):
        """
        Create Bouquet.
        """
        incoming_data = BouquetInputSerializer(data=request.data)
        incoming_data.is_valid(raise_exception=True)

        try:
            bouquet = self.service.create(incoming_data.validated_data)

            output_serializer = BouquetOutputSerializer(bouquet)
            return Response(output_serializer.data, status=HTTP_201_CREATED)
        except (ObjectDoesNotExistError, ValidationError) as e:
            return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=BouquetUpdateSerializer,
        responses={
            200: OpenApiResponse(response=BouquetOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
        },
        tags=GROUP_TAG
    )
    def update(self, request, pk):
        """
        Update Bouquet.
        """
        incoming_data = BouquetUpdateSerializer(data=request.data)
        incoming_data.is_valid(raise_exception=True)

        try:
            bouquet = self.service.update(pk, incoming_data.validated_data)

            output_serializer = BouquetOutputSerializer(bouquet)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=None,
        responses={
            200: OpenApiResponse(response=BouquetOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
            409: OpenApiResponse(description="Resource cannot be deleted: it has linked data")
        },
        tags=GROUP_TAG
    )
    def destroy(self, request, pk):
        """
        Delete Bouquet.
        """
        try:
            deleted_bouquet = self.service.delete(pk)

            output_serializer = BouquetOutputSerializer(deleted_bouquet)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
        except ObjectCannotBeDeletedError as e:
            return Response({"message": e.message}, status=HTTP_409_CONFLICT)

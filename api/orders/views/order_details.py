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
    OrderDetailsOutputSerializer,
    OrderDetailsInputSerializer,
    OrderDetailsUpdateSerializer,
)
from app_services.orders import OrderDetailsService
from domain.core.exceptions import (
    ObjectDoesNotExistError,
    ObjectCannotBeDeletedError,
)


class OrderDetailsViewSet(ViewSet):
    GROUP_TAG = ["order_details"]

    """
    Order Details view.
    """

    def __init__(
            self, service: OrderDetailsService = OrderDetailsService(),
            **kwargs
    ):
        super(OrderDetailsViewSet, self).__init__(**kwargs)
        self.service = service

    def dispatch(self, request, *args, **kwargs):
        return super(OrderDetailsViewSet, self).dispatch(request, *args, **kwargs)

    @inject
    def setup(
            self, request, service: OrderDetailsService = OrderDetailsService(),
            *args, **kwargs
    ):
        super(OrderDetailsViewSet, self).setup(request, service, args, kwargs)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=None,
        responses={
            200: OpenApiResponse(response=OrderDetailsOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
        },
        tags=GROUP_TAG
    )
    def retrieve(self, request, pk):
        """
        Get Order Details.
        """
        try:
            order_details = self.service.get_by_id(pk)

            output_serializer = OrderDetailsOutputSerializer(order_details)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)

    @extend_schema(
        request=None,
        responses={
            200: OpenApiResponse(response=OrderDetailsOutputSerializer(many=True)),
            400: OpenApiResponse(description="Bad request"),
        },
        tags=GROUP_TAG
    )
    def list(self, request):
        """
        Get all Orders Details.
        """
        order_details = self.service.get_all()

        output_serializer = OrderDetailsOutputSerializer(order_details, many=True)
        return Response(output_serializer.data, status=HTTP_200_OK)

    @extend_schema(
        parameters=None,
        request=OrderDetailsInputSerializer,
        responses={
            201: OpenApiResponse(response=OrderDetailsOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
        },
        tags=GROUP_TAG
    )
    def create(self, request):
        """
        Create Order Details.
        """
        incoming_data = OrderDetailsInputSerializer(data=request.data)
        incoming_data.is_valid(raise_exception=True)

        try:
            order_details = self.service.create(incoming_data.validated_data)

            output_serializer = OrderDetailsOutputSerializer(order_details)
            return Response(output_serializer.data, status=HTTP_201_CREATED)
        except (ObjectDoesNotExistError, ValidationError) as e:
            return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=OrderDetailsUpdateSerializer,
        responses={
            200: OpenApiResponse(response=OrderDetailsOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
        },
        tags=GROUP_TAG
    )
    def update(self, request, pk):
        """
        Update Order Details.
        """
        incoming_data = OrderDetailsUpdateSerializer(data=request.data)
        incoming_data.is_valid(raise_exception=True)

        try:
            order_details = self.service.update(pk, incoming_data.validated_data)

            output_serializer = OrderDetailsOutputSerializer(order_details)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=None,
        responses={
            200: OpenApiResponse(response=OrderDetailsOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
            409: OpenApiResponse(description="Resource cannot be deleted: it has linked data")
        },
        tags=GROUP_TAG
    )
    def destroy(self, request, pk):
        """
        Delete Order Details.
        """
        try:
            deleted_order_details = self.service.delete(pk)

            output_serializer = OrderDetailsOutputSerializer(deleted_order_details)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
        except ObjectCannotBeDeletedError as e:
            return Response({"message": e.message}, status=HTTP_409_CONFLICT)

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
    DiscountOutputSerializer,
    DiscountInputSerializer,
    DiscountUpdateSerializer,
)
from app_services.users import DiscountService
from domain.core.exceptions import (
    ObjectDoesNotExistError,
    ObjectCannotBeDeletedError,
)


class DiscountViewSet(ViewSet):
    GROUP_TAG = ["discounts"]

    """
    Discount view.
    """

    def __init__(
            self, service: DiscountService = DiscountService(),
            **kwargs
    ):
        super(DiscountViewSet, self).__init__(**kwargs)
        self.service = service

    def dispatch(self, request, *args, **kwargs):
        return super(DiscountViewSet, self).dispatch(request, *args, **kwargs)

    @inject
    def setup(
            self, request, service: DiscountService = DiscountService(),
            *args, **kwargs
    ):
        super(DiscountViewSet, self).setup(request, service, args, kwargs)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=None,
        responses={
            200: OpenApiResponse(response=DiscountOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
        },
        tags=GROUP_TAG
    )
    def retrieve(self, request, pk):
        """
        Get Discount.
        """
        try:
            discount = self.service.get_by_id(pk)

            output_serializer = DiscountOutputSerializer(discount)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)

    @extend_schema(
        request=None,
        responses={
            200: OpenApiResponse(response=DiscountOutputSerializer(many=True)),
            400: OpenApiResponse(description="Bad request"),
        },
        tags=GROUP_TAG
    )
    def list(self, request):
        """
        Get all Discounts.
        """
        discounts = self.service.get_all()

        output_serializer = DiscountOutputSerializer(discounts, many=True)
        return Response(output_serializer.data, status=HTTP_200_OK)

    @extend_schema(
        parameters=None,
        request=DiscountInputSerializer,
        responses={
            201: OpenApiResponse(response=DiscountOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
        },
        tags=GROUP_TAG
    )
    def create(self, request):
        """
        Create Discount.
        """
        incoming_data = DiscountInputSerializer(data=request.data)
        incoming_data.is_valid(raise_exception=True)

        try:
            discount = self.service.create(incoming_data.validated_data)

            output_serializer = DiscountOutputSerializer(discount)
            return Response(output_serializer.data, status=HTTP_201_CREATED)
        except (ObjectDoesNotExistError, ValidationError) as e:
            return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=DiscountUpdateSerializer,
        responses={
            200: OpenApiResponse(response=DiscountOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
        },
        tags=GROUP_TAG
    )
    def update(self, request, pk):
        """
        Update Discount.
        """
        incoming_data = DiscountUpdateSerializer(data=request.data)
        incoming_data.is_valid(raise_exception=True)

        try:
            discount = self.service.update(pk, incoming_data.validated_data)

            output_serializer = DiscountOutputSerializer(discount)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response({"message": e.message}, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[OpenApiParameter("id", OpenApiTypes.UUID, OpenApiParameter.PATH)],
        request=None,
        responses={
            200: OpenApiResponse(response=DiscountOutputSerializer),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Resource not found"),
            409: OpenApiResponse(description="Resource cannot be deleted: it has linked data")
        },
        tags=GROUP_TAG
    )
    def destroy(self, request, pk):
        """
        Delete Discount.
        """
        try:
            deleted_discount = self.service.delete(pk)

            output_serializer = DiscountOutputSerializer(deleted_discount)
            return Response(output_serializer.data, status=HTTP_200_OK)
        except ObjectDoesNotExistError as e:
            return Response({"message": e.message}, status=HTTP_404_NOT_FOUND)
        except ObjectCannotBeDeletedError as e:
            return Response({"message": e.message}, status=HTTP_409_CONFLICT)

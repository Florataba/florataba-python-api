from injector import inject

from app_services.users import LocationService
from domain.core import Singleton
from domain.core.exceptions import (
    ObjectMustBeLinkedError,
    ObjectDoesNotExistError,
)
from domain.core.services import BaseService
from domain.orders.models import OrderDetails
from domain.orders.repositories import OrderDetailsRepository
from domain.users.models import Location


class OrderDetailsService(BaseService, metaclass=type(Singleton)):
    BASE_CLASS = OrderDetails
    BASE_REPO = OrderDetailsRepository

    @inject
    def __init__(
            self, repo: OrderDetailsRepository = OrderDetailsRepository()
    ):
        super().__init__()
        self.repo = repo

    @classmethod
    def _link_location_entity(cls, data: dict, on_create: bool = False) -> dict:
        address_id = data.get("address_id")
        if not address_id and on_create:
            raise ObjectMustBeLinkedError(
                OrderDetails,
                link_to=[Location],
            )
        elif not address_id and not on_create:
            return data

        address = LocationService().get_by_id(address_id)
        if not address:
            raise ObjectDoesNotExistError(
                Location,
                id=address_id
            )
        data["address"] = address
        data.pop("address_id")
        return data

    def create(self, data: dict) -> OrderDetails:
        data = self._link_location_entity(data, on_create=True)
        return super().create(data)

    def update(self, order_details_id: str, data: dict) -> OrderDetails:
        data = self._link_location_entity(data)
        return super().update(order_details_id, data)

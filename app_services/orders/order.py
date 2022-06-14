from injector import inject

from app_services.orders import OrderDetailsService
from domain.core import Singleton
from domain.core.exceptions import (
    ObjectDoesNotExistError,
)
from domain.core.services import BaseService
from domain.orders import OrderDetails
from domain.orders.models import Order
from domain.orders.repositories import OrderRepository


class OrderService(BaseService, metaclass=type(Singleton)):
    BASE_CLASS = Order
    BASE_REPO = OrderRepository

    @inject
    def __init__(
            self, repo: OrderRepository = OrderRepository()
    ):
        super().__init__()
        self.repo = repo

    @classmethod
    def _link_order_details_entity(cls, data: dict, on_create: bool = False) -> dict:
        order_details_id = data.get("order_details_id")
        if not order_details_id and on_create:
            return data
        elif not order_details_id and not on_create:
            return data

        order_details = OrderDetailsService().get_by_id(order_details_id)
        if not order_details:
            raise ObjectDoesNotExistError(
                OrderDetails,
                id=order_details_id
            )
        data["order_details"] = order_details
        data.pop("order_details_id")
        return data

    def create(self, data: dict) -> Order:
        data = self._link_order_details_entity(data, on_create=True)
        return super().create(data)

    def update(self, order_id: str, data: dict) -> Order:
        data = self._link_order_details_entity(data)
        return super().update(order_id, data)

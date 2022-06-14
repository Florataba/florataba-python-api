from injector import inject

from app_services.users import (
    DiscountService,
    LocationService,
)
from domain.core import Singleton
from domain.core.exceptions import (
    ObjectMustBeLinkedError,
    ObjectDoesNotExistError,
)
from domain.core.services import BaseService
from domain.users.models import (
    UserDetails,
    Discount,
    Location,
)
from domain.users.repositories import UserDetailsRepository


class UserDetailsService(BaseService, metaclass=type(Singleton)):
    BASE_CLASS = UserDetails
    BASE_REPO = UserDetailsRepository

    @inject
    def __init__(
            self, repo: UserDetailsRepository = UserDetailsRepository()
    ):
        super().__init__()
        self.repo = repo

    @classmethod
    def _link_discount_entity(cls, data: dict, on_create: bool = False) -> dict:
        discount_id = data.get("discount_id")
        if not discount_id and on_create:
            raise ObjectMustBeLinkedError(
                UserDetails,
                link_to=[Discount],
            )
        elif not discount_id and not on_create:
            return data

        discount = DiscountService().get_by_id(discount_id)
        if not discount:
            raise ObjectDoesNotExistError(
                Discount,
                id=discount_id
            )
        data["discount"] = discount
        data.pop("discount_id")
        return data

    @classmethod
    def _link_location_entity(cls, data: dict, on_create: bool = False) -> dict:
        delivery_address_id = data.get("delivery_address_id")
        if not delivery_address_id and on_create:
            raise ObjectMustBeLinkedError(
                UserDetails,
                link_to=[Location],
            )
        elif not delivery_address_id and not on_create:
            return data

        delivery_address = LocationService().get_by_id(delivery_address_id)
        if not delivery_address:
            raise ObjectDoesNotExistError(
                Location,
                id=delivery_address_id
            )
        data["delivery_address"] = delivery_address
        data.pop("delivery_address_id")
        return data

    def create(self, data: dict) -> UserDetails:
        data = self._link_discount_entity(data, on_create=True)
        data = self._link_location_entity(data, on_create=True)
        return super().create(data)

    def update(self, user_details_id: str, data: dict) -> UserDetails:
        data = self._link_discount_entity(data)
        data = self._link_location_entity(data)
        return super().update(user_details_id, data)

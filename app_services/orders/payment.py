from injector import inject

from app_services.users import UserDetailsService
from domain.core import Singleton
from domain.core.exceptions import ObjectDoesNotExistError
from domain.core.services import BaseService
from domain.orders.models import Payment
from domain.orders.repositories import PaymentRepository
from domain.users.models import UserDetails


class PaymentService(BaseService, metaclass=type(Singleton)):
    BASE_CLASS = Payment
    BASE_REPO = PaymentRepository

    @inject
    def __init__(
            self, repo: PaymentRepository = PaymentRepository()
    ):
        super().__init__()
        self.repo = repo

    @classmethod
    def _link_user_details_entity(cls, data: dict) -> dict:
        user_id = data.get("user_id")
        if user_id:
            user_details = UserDetailsService().get_by_id(user_id)
            if not user_details:
                raise ObjectDoesNotExistError(
                    UserDetails,
                    id=user_id
                )
            data["user"] = user_details
            data.pop("user_id")
        return data

    def create(self, data: dict) -> Payment:
        data = self._link_user_details_entity(data)
        return super().create(data)

    def update(self, payment_id: str, data: dict) -> Payment:
        data = self._link_user_details_entity(data)
        return super().update(payment_id, data)

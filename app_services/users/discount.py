from injector import inject

from domain.core import Singleton
from domain.core.services import BaseService
from domain.users.models import Discount
from domain.users.repositories import DiscountRepository


class DiscountService(BaseService, metaclass=type(Singleton)):
    BASE_CLASS = Discount
    BASE_REPO = DiscountRepository

    @inject
    def __init__(
            self, repo: DiscountRepository = DiscountRepository()
    ):
        super().__init__()
        self.repo = repo

    def create(self, data: dict) -> Discount:
        return super().create(data)

    def update(self, discount_id: str, data: dict) -> Discount:
        return super().update(discount_id, data)

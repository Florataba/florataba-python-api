from injector import inject

from domain.core import Singleton
from domain.core.services import BaseService
from domain.orders.models import Bouquet
from domain.orders.repositories import BouquetRepository


class BouquetService(BaseService, metaclass=type(Singleton)):
    BASE_CLASS = Bouquet
    BASE_REPO = BouquetRepository

    @inject
    def __init__(
            self, repo: BouquetRepository = BouquetRepository()
    ):
        super().__init__()
        self.repo = repo

    def create(self, data: dict) -> Bouquet:
        return super().create(data)

    def update(self, bouquet_id: str, data: dict) -> Bouquet:
        return super().update(bouquet_id, data)

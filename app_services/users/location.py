from injector import inject

from domain.core import Singleton
from domain.core.services import BaseService
from domain.users.models import Location
from domain.users.repositories import LocationRepository


class LocationService(BaseService, metaclass=type(Singleton)):
    BASE_CLASS = Location
    BASE_REPO = LocationRepository

    @inject
    def __init__(
            self, repo: LocationRepository = LocationRepository()
    ):
        super().__init__()
        self.repo = repo

    def create(self, data: dict) -> Location:
        return super().create(data)

    def update(self, location_id: str, data: dict) -> Location:
        return super().update(location_id, data)

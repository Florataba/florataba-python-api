from abc import (
    ABC,
    abstractmethod,
)
from typing import Optional

from django.db.models import QuerySet

from domain.core import Singleton
from domain.core.exceptions import (
    ObjectDoesNotExistError,
    ObjectCannotBeDeletedError,
)
from domain.core.repositories import BaseRepository
from domain.core.models import BaseUUIDModel


class BaseService(ABC, metaclass=type(Singleton)):
    """
    Base service class implementation.
    """
    BASE_CLASS = BaseUUIDModel
    BASE_REPO = BaseRepository

    def __init__(self):
        self.repo = self.BASE_REPO()

    def get_all(self) -> Optional[QuerySet[BASE_CLASS]]:
        return self.repo.get_all()

    def get_by_id(self, obj_id: str) -> Optional[BASE_CLASS]:
        obj = self.repo.get_by_id(obj_id)
        if not obj:
            raise ObjectDoesNotExistError(
                self.BASE_CLASS, obj_id
            )
        return obj

    @abstractmethod
    def create(self, data: dict) -> BASE_CLASS:
        # provide your own implementation for subclasses or just call super().create(...)
        return self.repo.create(data)

    @abstractmethod
    def update(self, obj_id: str, data: dict) -> BASE_CLASS:
        # provide your own implementation for subclasses or just call super().update(...)
        obj = self.repo.get_by_id(obj_id)
        if not obj:
            raise ObjectDoesNotExistError(
                self.BASE_CLASS, obj_id
            )
        return self.repo.update(obj, data)

    def delete(self, obj_id: str) -> Optional[BASE_CLASS]:
        obj = self.repo.get_by_id(obj_id)
        if not obj:
            raise ObjectDoesNotExistError(
                self.BASE_CLASS, obj_id
            )
        deleted_obj = self.repo.delete_obj(obj)
        if not deleted_obj:
            raise ObjectCannotBeDeletedError(
                self.BASE_CLASS, obj_id
            )
        else:
            return deleted_obj

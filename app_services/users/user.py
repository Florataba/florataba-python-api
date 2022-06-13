from injector import inject

from app_services.users import UserDetailsService
from domain.core import Singleton
from domain.core.exceptions import (
    ObjectMustBeLinkedError,
    ObjectDoesNotExistError,
)
from domain.core.services import BaseService
from domain.users.models import (
    User,
    UserDetails,
)
from domain.users.repositories import UserRepository


class UserService(BaseService, metaclass=type(Singleton)):
    BASE_CLASS = User
    BASE_REPO = UserRepository

    @inject
    def __init__(
            self, repo: UserRepository = UserRepository()
    ):
        super().__init__()
        self.repo = repo

    @classmethod
    def _link_user_details_entity(cls, data: dict, on_create: bool = False) -> dict:
        details_id = data.get("details_id")
        if not details_id and on_create:
            raise ObjectMustBeLinkedError(
                User,
                link_to=[UserDetails],
            )
        elif not details_id and not on_create:
            return data

        user_details = UserDetailsService().get_by_id(details_id)
        if not user_details:
            raise ObjectDoesNotExistError(
                UserDetails,
                id=details_id
            )
        data["details_id"] = user_details
        return data

    def create(self, data: dict) -> User:
        data = self._link_user_details_entity(data, on_create=True)
        return super().create(data)

    def update(self, user_id: str, data: dict) -> User:
        data = self._link_user_details_entity(data)
        return super().update(user_id, data)

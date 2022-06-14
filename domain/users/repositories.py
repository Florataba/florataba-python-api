from typing import Optional

from domain.core import (
    BaseRepository,
    Singleton,
)
from domain.users.models import (
    Discount,
    Location,
    User,
    UserDetails,
)


class DiscountRepository(BaseRepository, metaclass=type(Singleton)):
    BASE_CLASS = Discount


class LocationRepository(BaseRepository, metaclass=type(Singleton)):
    BASE_CLASS = Location


class UserRepository(BaseRepository, metaclass=type(Singleton)):
    BASE_CLASS = User

    def get_by_id(self, object_id: str) -> Optional[BASE_CLASS]:
        try:
            return self.BASE_CLASS.objects.get(email=object_id)
        except self.BASE_CLASS.DoesNotExist:
            return None


class UserDetailsRepository(BaseRepository, metaclass=type(Singleton)):
    BASE_CLASS = UserDetails

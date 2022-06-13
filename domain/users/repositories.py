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


class UserDetailsRepository(BaseRepository, metaclass=type(Singleton)):
    BASE_CLASS = UserDetails

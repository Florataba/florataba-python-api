from domain.core import (
    BaseRepository,
    Singleton,
)
from domain.internal.models import Notification


class NotificationRepository(BaseRepository, metaclass=type(Singleton)):
    BASE_CLASS = Notification

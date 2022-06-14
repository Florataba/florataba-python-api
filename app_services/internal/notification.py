from injector import inject

from domain.core import Singleton
from domain.core.services import BaseService
from domain.internal.models import Notification
from domain.internal.repositories import NotificationRepository


class NotificationService(BaseService, metaclass=type(Singleton)):
    BASE_CLASS = Notification
    BASE_REPO = NotificationRepository

    @inject
    def __init__(
            self, repo: NotificationRepository = NotificationRepository()
    ):
        super().__init__()
        self.repo = repo

    def create(self, data: dict) -> Notification:
        return super().create(data)

    def update(self, notification_id: str, data: dict) -> Notification:
        return super().update(notification_id, data)

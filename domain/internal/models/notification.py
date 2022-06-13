from django.db import models

from domain.core.models import (
    BaseUUIDModel,
    NotificationType,
)


class Notification(BaseUUIDModel):
    type = models.CharField(max_length=50, choices=NotificationType.choices, null=True, blank=True)
    text = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

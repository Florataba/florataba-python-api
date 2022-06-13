from django.db import models

from domain.core import BaseUUIDModel, NotificationType


class Notification(BaseUUIDModel):
    type = models.CharField(max_length=50, choices=NotificationType.choices, null=True, blank=True)
    text = models.CharField(max_length=255, null=False)

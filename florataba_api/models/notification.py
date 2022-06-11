from django.db import models
from florataba_api.models.utils import NotificationType


class Notification(models.Model):
    type = models.CharField(choices=NotificationType.choices, on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=255, null=False)

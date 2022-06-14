from django.db import models

from domain.core.models import BaseUUIDModel
from domain.users.models import (
    Discount,
    Location,
)


class UserDetails(BaseUUIDModel):
    discount = models.ForeignKey(Discount, null=False, on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User Details'
        verbose_name_plural = 'Users Details'

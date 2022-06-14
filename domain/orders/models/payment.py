from django.db import models

from domain.core.models import BaseUUIDModel
from domain.users.models import (
    User,
    UserDetails,
)


class Payment(BaseUUIDModel):
    card_number = models.CharField(max_length=16, null=False)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True)
    cvv = models.CharField(max_length=3, null=False)
    placeholder_name = models.CharField(max_length=80, null=True)
    bank_name = models.CharField(max_length=20, null=False)
    expiration_date = models.DateField()

    class Meta:
        verbose_name = 'User Details'
        verbose_name_plural = 'Users Details'

    def set_card_owner(self, user: User):
        self.user = user

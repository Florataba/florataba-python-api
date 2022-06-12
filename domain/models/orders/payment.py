from django.db import models

from domain.models.core import BaseUUIDModel
from domain.models.users import UserDetails


class Payment(BaseUUIDModel):
    card_number = models.CharField(max_length=16, null=False)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True)
    cvv = models.CharField(max_length=3, null=False)
    placeholder_name = models.CharField(max_length=80, null=True)
    bank_name = models.CharField(max_length=20, null=False)
    expiration_date = models.DateField()

    def set_placeholder_name(self, user):
        self.placeholder_name = f"{user.first_name} {user.surname}"
        return True

    def set_card_owner(self, user):
        self.user = user

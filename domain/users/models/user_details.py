from django.db import models

from domain.core import BaseUUIDModel
from domain.users import (
    Discount,
    Location,
)


class UserDetails(BaseUUIDModel):
    discount = models.ForeignKey(Discount, null=False, on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)

    def get_user_data(self):
        pass

    def update_user_data(self, data):
        pass

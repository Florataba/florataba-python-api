from django.core.validators import MinValueValidator
from django.db import models

from domain.models.core import BaseUUIDModel, DiscountType


class Discount(BaseUUIDModel):
    type = models.IntegerField(choices=DiscountType.choices, null=False)
    benefits_text = models.CharField(max_length=255, null=False)
    discount_percent = models.DecimalField(
        validators=[MinValueValidator(0)], max_digits=5, decimal_places=2, null=False
    )

    def update_discount_type(self, discount_type):
        self.type = discount_type

    def get_discount_info(self):
        return self.discount_percent

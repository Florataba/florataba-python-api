from django.core.validators import MinValueValidator
from django.db import models

from domain.core.models import (
    BaseUUIDModel,
    DiscountType,
)


class Discount(BaseUUIDModel):
    type = models.IntegerField(choices=DiscountType.choices, null=False)
    benefits_text = models.CharField(max_length=255, null=False)
    discount_percent = models.DecimalField(
        validators=[MinValueValidator(0)], max_digits=5, decimal_places=2, null=False
    )

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'

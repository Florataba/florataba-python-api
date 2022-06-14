from django.db import models

from domain.core.models import BaseUUIDModel
from domain.users.models import Location


class OrderDetails(BaseUUIDModel):
    order_info = models.CharField(max_length=255, null=True)
    address = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, null=False)

    class Meta:
        verbose_name = 'Order Details'
        verbose_name_plural = 'Orders Details'

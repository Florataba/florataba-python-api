from django.db import models
from domain.orders.models import OrderDetails
from domain.core.models import (
    BaseUUIDModel,
    OrderStatus,
)


class Order(BaseUUIDModel):
    status = models.CharField(max_length=50, choices=OrderStatus.choices, null=False)
    order_details = models.ForeignKey(OrderDetails, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def get_order_info(self):
        return self.order_details

    def add_order(self, order):
        pass

from django.db import models
from florataba_api.models.order_details import OrderDetails
from florataba_api.models.utils import OrderStatus


class Order(models.Model):
    creation_date = models.DateField()
    status = models.CharField(choices=OrderStatus.choices, null=False)
    order_details = models.ForeignKey(OrderDetails, on_delete=models.DO_NOTHING)

    def get_order_info(self):
        return self.order_details

    def add_order(self, order):
        pass

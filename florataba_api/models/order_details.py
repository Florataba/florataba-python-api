from django.db import models
from florataba_api.models.location import Location


class OrderDetails(models.Model):
    order_info = models.CharField(max_length=255, null=True)
    address = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_length=5, decimal_places=2, null=False)

from django.db import models
from utils import DiscountType


class Discount(models.Model):
    type = models.IntegerField(DiscountType, null=False)
    benefits_text = models.CharField(max_length=255, null=False)
    discount_percent = models.FloatField(max_length=5, null=False)

    def update_discount_type(self, discount_type):
        self.type = discount_type

    def get_discount_info(self):
        return self.discount_percent

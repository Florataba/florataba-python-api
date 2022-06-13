from django.core.validators import MinValueValidator
from django.db import models

from domain.core import BaseUUIDModel, EventTypeBouquet


class Bouquet(BaseUUIDModel):
    title = models.CharField(max_length=32, null=False)
    event_type_bouquet = models.CharField(
        max_length=36, choices=EventTypeBouquet.choices, default=EventTypeBouquet.SINGLE
    )
    description = models.TextField(max_length=1000, null=False)
    price = models.DecimalField(
        validators=[MinValueValidator(0)], max_digits=5, decimal_places=2, null=False
    )
    is_single_bouquet = models.BooleanField(default=True)
    available_quantity = models.IntegerField(validators=[MinValueValidator(1)])
    img_url = models.CharField(max_length=255, null=False)

    def get_bouquet_for_event(self, event_type):
        pass

    def get_bouquet_description(self):
        return self.description

    def get_bouquet_list(self):
        pass

    def add_bouquet_to_order(self):
        pass

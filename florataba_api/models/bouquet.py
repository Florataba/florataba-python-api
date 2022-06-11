from django.db import models
from florataba_api.models.utils import EventType


class Bouquet(models.Model):
    title = models.CharField(max_length=32, null=False)
    event_type = models.CharField(choices=EventType.choices, null=False)
    description = models.CharField(max_length=64, null=False)
    price = models.DecimalField(decimal_places=2, null=False)
    is_single_bouquet = models.BooleanField(default=True)
    available_quantity = models.IntegerField(max_length=100)
    img_url = models.CharField(max_length=255, null=False)

    def get_bouquet_for_event(self, event_type):
        pass

    def get_bouquet_description(self):
        return self.description

    def get_bouquet_list(self):
        pass

    def add_bouquet_to_order(self):
        pass

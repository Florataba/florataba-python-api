from django.db import models

from domain.models.core import BaseUUIDModel


class Location(BaseUUIDModel):
    street = models.CharField(max_length=64, null=True, blank=True)
    region = models.CharField(max_length=32, null=True, blank=True)
    build_number = models.CharField(max_length=10, null=False)
    apartment_number = models.CharField(max_length=10, null=False)

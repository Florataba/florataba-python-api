from django.db import models


class Location(models.Model):
    street = models.CharField(max_length=64, null=True)
    region = models.CharField(max_length=32, null=True)
    build_number = models.CharField(max_length=10, null=False, primary_key=True)
    apartment_number = models.CharField(max_length=10, null=False)

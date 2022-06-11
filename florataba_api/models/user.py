from django.db import models
from florataba_api.models.user_details import UserDetails


class User(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=80, null=False, primary_key=True)
    phone_number = models.CharField(max_length=20, null=False)
    details_id = models.ForeignKey(UserDetails, null=False, on_delete=models.CASCADE)
    __password = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f"Email: {self.email}"

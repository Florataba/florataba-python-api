from django.core.validators import EmailValidator, MinLengthValidator
from django.db import models

from domain.users import UserDetails


class User(models.Model):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    surname = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(validators=[EmailValidator()], null=False, blank=False, unique=True, primary_key=True)
    phone_number = models.CharField(max_length=20, null=False)
    details_id = models.ForeignKey(UserDetails, null=False, on_delete=models.CASCADE)
    __password = models.CharField(max_length=64, null=False, validators=[MinLengthValidator(5)])

    def __str__(self):
        return f"Email: {self.email}"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.surname}"

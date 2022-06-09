from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=80, null=False, primary_key=True)
    phone_number = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=20, null=False)

    def call_help_center(self):
        return f"You make request to Insurance " \
               f"CallCenter by email:{self.email} as {self.first_name} {self.surname}"

    def __str__(self):
        return f"Email:{self.email}"


class Document(models.Model):
    card_id = models.CharField(max_length=30, null=True)
    itn = models.CharField(max_length=30, null=True)
    place_issue = models.CharField(max_length=20, null=False)
    expiration_date = models.CharField(max_length=20, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

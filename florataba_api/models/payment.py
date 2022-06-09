from django.db import models

from florataba_api.models.user import User


class Payment(models.Model):
    card_number = models.CharField(max_length=30, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cvv = models.CharField(max_length=3, null=False)
    placeholder_name = models.CharField(max_length=80, null=True)
    bank_name = models.CharField(max_length=20, null=False)
    expiration_date = models.CharField(max_length=20, null=False)

    def set_placeholder_name(self, user):
        self.placeholder_name = f"{user.firs_name} {user.surname}"
        return True

    def set_card_owner(self, user):
        self.user = user
        return True

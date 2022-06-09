from django.db import models

from florataba_api.models.user import User


class InsuranceData(models.Model):
    condition = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=90, null=True)
    price = models.CharField(max_length=30, null=False)
    is_available = models.BooleanField(null=True, default=True)
    title = models.CharField(max_length=666, null=False)
    reserved_by_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def synk_insurance_to_user(self, user, available_status):
        self.reserved_by_user = user
        self.is_available = available_status
        return True

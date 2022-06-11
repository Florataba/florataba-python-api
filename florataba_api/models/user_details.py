from django.db import models
from florataba_api.models.discount import Discount
from florataba_api.models.payment import Payment
from florataba_api.models.location import Location


class UserDetails(models.Model):
    discount = models.ForeignKey(Discount, null=False, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, null=False, on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)

    def get_user_data(self):
        pass

    def update_user_data(self, data):
        pass

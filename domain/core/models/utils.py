from django.db import models
from django.utils.translation import gettext_lazy as _


class DiscountType(models.IntegerChoices):
    GOLD = 50, 'Gold'
    START = 5, 'Start'
    FAMILY = 15, 'Family'
    VOLUNTEER = 20, 'Volunteer'


class EventTypeBouquet(models.TextChoices):
    WEDDINGS = 'Wedding', _('Wedding')
    BIRTHDAYS = 'Birthday', _('Birthday')
    VALENTINES_DAY = 'Valentine\'s Day', _('Valentine\'s Day')
    FUNERAL = 'Funeral', _('Funeral')
    SINGLE = 'Single', _('Single')


class OrderStatus(models.TextChoices):
    COLLECTING = 'Collecting'
    IN_WAY = 'En route'
    DONE = 'Done'
    PROCESSED = 'Processed'


class NotificationType(models.TextChoices):
    NEWS = 'News'
    ORDERS = 'Orders'
    DISCOUNT = 'Discounts'

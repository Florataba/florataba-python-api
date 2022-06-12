from django.db import models


class DiscountType(models.IntegerChoices):
    GOLD = 50
    START = 5
    FAMILY = 15
    VOLUNTEER = 20


class EventType(models.TextChoices):
    WEDDINGS = 'Wedding'
    BIRTHDAYS = 'Birthday'
    VALENTINES_DAY = 'Valentine\'s Day'
    FUNERAL = 'Funeral'
    SINGLE = 'Single'


class OrderStatus(models.TextChoices):
    COLLECTING = 'Collecting'
    IN_WAY = 'En route'
    DONE = 'Done'
    PROCESSED = 'Processed'


class NotificationType(models.TextChoices):
    NEWS = 'News'
    ORDERS = 'Orders'
    DISCOUNT = 'Discounts'

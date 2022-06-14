from django.contrib import admin
from domain.internal.models import (
    Notification,
)
from domain.users.models import (
    Discount,
    Location,
    UserDetails,
    User,
)
from domain.orders.models import (
    Bouquet,
    OrderDetails,
    Order,
    Payment,
)

admin.site.register(Notification)

admin.site.register(Discount)
admin.site.register(Location)
admin.site.register(UserDetails)
admin.site.register(User)

admin.site.register(Bouquet)
admin.site.register(OrderDetails)
admin.site.register(Order)
admin.site.register(Payment)

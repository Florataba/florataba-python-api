from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from api.internal.views import NotificationViewSet
from api.orders.views import (
    BouquetViewSet,
    OrderDetailsViewSet,
    OrderViewSet,
    PaymentViewSet,
)
from api.users.views import (
    DiscountViewSet,
    LocationViewSet,
    UserViewSet,
    UserDetailsViewSet,
)

router = routers.SimpleRouter()

# Notifications
router.register(r"notifications", NotificationViewSet, basename="notifications")

# Orders
router.register(r"bouquet", BouquetViewSet, basename="bouquets")
router.register(r"order", OrderViewSet, basename="orders")
router.register(r"order-details", OrderDetailsViewSet, basename="order-details")
router.register(r"payment", PaymentViewSet, basename="payments")

# Users
router.register(r"discount", DiscountViewSet, basename="discounts")
router.register(r"location", LocationViewSet, basename="locations")
router.register(r"user", UserViewSet, basename="users")
router.register(r"user-details", UserDetailsViewSet, basename="user-details")


urlpatterns = [
    path(r"", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

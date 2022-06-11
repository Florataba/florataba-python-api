"""florataba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from florataba_api.views.user_view import *
from florataba_api.views.user_details_view import *
from florataba_api.views.bouquet_view import *
from florataba_api.views.discount_view import *
from florataba_api.views.location_view import *
from florataba_api.views.notification_view import *
from florataba_api.views.order_view import *
from florataba_api.views.order_details_view import *
from florataba_api.views.payment_view import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', UserListCreateAPIView.as_view()),
    path('users/<str:pk>/', UserRetrieveUpdateAPIView.as_view()),

    path('payments/', PaymentListCreateAPIView.as_view()),
    path('payments/<int:pk>/', PaymentRetrieveUpdateAPIView.as_view()),

    path('bouquetes/', BouquetListCreateAPIView.as_view()),
    path('bouquetes/<int:pk>/', BouquetRetrieveUpdateAPIView.as_view()),

    path('discounts/', DiscountListCreateAPIView.as_view()),
    path('discounts/<int:pk>/', DiscountRetrieveUpdateAPIView.as_view()),

    path('locations/', LocationListCreateAPIView.as_view()),
    path('locations/<int:pk>/', LocationRetrieveUpdateAPIView.as_view()),

    path('notifications/', NotificationListCreateAPIView.as_view()),
    path('notifications/<int:pk>/', NotificationRetrieveUpdateAPIView.as_view()),

    path('order_details/', OrderDetailsListCreateAPIView.as_view()),
    path('order_details/<int:pk>/', OrderDetailsRetrieveUpdateAPIView.as_view()),

    path('orders/', OrderListCreateAPIView.as_view()),
    path('orders/<int:pk>/', OrderRetrieveUpdateAPIView.as_view()),

    path('user_details/', UserDetailsListCreateAPIView.as_view()),
    path('user_details/<int:pk>/', UserDetailsRetrieveUpdateAPIView.as_view()),

    path('payments/', PaymentListCreateAPIView.as_view()),
    path('payments/<int:pk>/', PaymentRetrieveUpdateAPIView.as_view()),
]

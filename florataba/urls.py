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

from florataba_api.views.payment_view import PaymentListCreateAPIView, PaymentRetrieveUpdateAPIView
from florataba_api.views.user_view import DocumentListCreateAPIView, DocumentRetrieveUpdateAPIView, \
    UserListCreateAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('documents/', DocumentListCreateAPIView.as_view()),
    path('documents/<int:pk>/', DocumentRetrieveUpdateAPIView.as_view()),

    path('users/', UserListCreateAPIView.as_view()),
    path('users/<str:pk>/', UserRetrieveUpdateAPIView.as_view()),

    path('payments/', PaymentListCreateAPIView.as_view()),
    path('payments/<int:pk>/', PaymentRetrieveUpdateAPIView.as_view()),
]

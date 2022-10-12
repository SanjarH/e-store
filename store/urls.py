from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart')
]

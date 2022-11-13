from django.urls import path
from .views import AddProductView

app_name = 'products'

urlpatterns = [
    path("add/", AddProductView.as_view(), name="add"),
    
]
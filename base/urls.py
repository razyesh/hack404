from django.urls import path, include
from . import views

app_name = "base"

urlpatterns = [
    path('', views.base, name="base"),
    path('add-to-cart', views.add_to_cart, name="add_to_cart")
]
from django.urls import path, include
from . import views

app_name = "product"

urlpatterns = [
    path('shop', views.shop, name="shop"),
    path('add-to-cart', views.add_to_cart, name="add-to-cart"),
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name="product-detail"),
    path('product-add', views.product_add, name="product-add"),
]
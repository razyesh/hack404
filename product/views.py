from django.shortcuts import render
from .models import Cart
from .forms import CartForm
from product.models import Product, Category

def add_to_cart(request):
    form = CartForm()
    return render(request, 'base.html', {'form':form})


def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop.html', {'products':products, 'categories':categories})
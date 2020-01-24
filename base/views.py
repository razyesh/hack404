from django.shortcuts import render
from product.models import Product

def base(request):
    products = Product.objects.all()
    return render(request, 'base.html', {'products':products})

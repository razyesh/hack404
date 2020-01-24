from django.shortcuts import render
from product.models import Product
from user.models import Seller

def base(request):
    products = Product.objects.all()
    return render(request, 'base.html', {'products':products})

def dashboard(request, id):
    users = Seller.objects.all()
    user_id = Seller.objects.get(id=id)
    return render(request, 'dashboard/demo_1/index.html', {'users':users, 'user_id':user_id})
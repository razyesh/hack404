from django.shortcuts import render
from product.models import Product

def base(request):
    products = Product.objects.all()
    return render(request, 'base.html', {'products':products})


def add_to_cart(request):
    if request.method== "POST":
        item_name = request.POST.get("item_name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        print(item_name)
        c = Cart(product_name = item_name, quantity=quantity, price=price)
        c.save()

    return render(request, 'base.html')
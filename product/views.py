from django.shortcuts import render
from .models import Cart
from .forms import CartForm

def add_to_cart(request):
    form = CartForm()
    return render(request, 'base.html', {'form':form})

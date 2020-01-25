from django.shortcuts import render
from .models import Cart
from .forms import CartForm
from product.models import Product, Category
from django.views.generic.detail import DetailView

def add_to_cart(request):
    form = CartForm()
    return render(request, 'base.html', {'form':form})


def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop.html', {'products':products, 'categories':categories})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

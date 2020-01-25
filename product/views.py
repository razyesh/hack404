from django.shortcuts import render, redirect
from .models import Cart
from .forms import CartForm, ProductAddForm
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

def product_add(request):
    print('Worked')
    if request.method == "POST":
        form = ProductAddForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redire('/product-add')

    else:
        form = ProductAddForm()
    return render(request, 'dashboard/add_product.html', {'form':form})
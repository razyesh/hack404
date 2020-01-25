from django import forms
from .models import Cart, Product

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart 
        fields = ['product_name', 'quantity', 'price']


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "slug",
            "item_type",
            "image",
            "price",
            "description",
        ]

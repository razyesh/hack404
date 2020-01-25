from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name 


class Product(models.Model):
    user = models.ForeignKey(User, related_name="product", on_delete = models.CASCADE)
    name = models.CharField(max_length= 20)
    slug = models.SlugField()
    item_type = models.ForeignKey(Category,related_name="Product", on_delete=models.PROTECT)
    image = models.ImageField(upload_to="product/media")
    price = models.FloatField()
    description = models.TextField(max_length=200)
    is_custom = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return f"/product/{self.slug}"

class Cart(models.Model):
    product_name = models.CharField(max_length=256)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.product_name


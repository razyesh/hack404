from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)


class Product(models.Model):
    name = models.CharField(max_length= 20)
    item_type = models.ForeignKey(Category,related_name="Product", on_delete=models.PROTECT)
    image = models.ImageField(upload_to="/product/media")
    price = models.FloatField()
    description = models.TextField(max_length=200)
    choice = models.BooleanField(default=False)


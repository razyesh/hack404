from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


CITY = [
    ("KATHMANDU", "Kathmandu"),
    ("BHAKTAPUR", "Bhaktapur"),
    ("LALITPUR", "Lalitpur")
]

PROVINCE = [
    ('1','Province 1'),
    ('2', 'Province 2'),
    ('3', 'Bagmati'),
    ('4', 'Gandaki'),
    ('5','Province 5'),
    ('6', 'Karnali'),
    ('7', 'Sudurpaschim'),
]
class Seller(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='user/seller')
    contact = models.IntegerField(validators=[MaxLengthValidator(10), MinLengthValidator(10)])
    street_address1 = models.CharField(max_length=256)
    street_address2 = models.CharField(max_length=256)
    city = models.CharField(choices=CITY, max_length=256)
    province = models.CharField(choices=PROVINCE, max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    



    
# Generated by Django 3.0.2 on 2020-01-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
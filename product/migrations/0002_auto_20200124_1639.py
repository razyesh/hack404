# Generated by Django 3.0.2 on 2020-01-24 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='choice',
            new_name='is_custom',
        ),
    ]

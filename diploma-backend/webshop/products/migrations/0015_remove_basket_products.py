# Generated by Django 4.2.10 on 2024-02-16 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_basket_products_alter_basket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='products',
        ),
    ]
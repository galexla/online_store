# Generated by Django 4.2.10 on 2024-03-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_order_orderproduct_order_products_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('online', 'online'), ('random', 'random')], max_length=15),
        ),
    ]

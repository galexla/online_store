# Generated by Django 4.2.10 on 2024-03-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_order_payment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(blank=True, choices=[('regular', 'regular'), ('express', 'express')], max_length=15),
        ),
    ]

# Generated by Django 4.2.10 on 2024-03-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_alter_order_delivery_type_alter_order_payment_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('processing', 'processing'), ('paid', 'paid')], default='new', max_length=15),
        ),
    ]
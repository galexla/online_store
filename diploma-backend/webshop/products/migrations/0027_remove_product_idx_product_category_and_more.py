# Generated by Django 4.2.10 on 2024-03-11 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_sale'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='product',
            name='idx_product_category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='purchases',
            new_name='sold_count',
        ),
    ]

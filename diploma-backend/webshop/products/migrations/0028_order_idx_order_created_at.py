# Generated by Django 4.2.10 on 2024-03-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_remove_product_idx_product_category_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['created_at'], name='idx_order_created_at'),
        ),
    ]

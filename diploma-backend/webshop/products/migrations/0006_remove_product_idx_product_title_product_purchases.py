# Generated by Django 4.2 on 2024-02-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_category_idx_category_parent_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='product',
            name='idx_product_title',
        ),
        migrations.AddField(
            model_name='product',
            name='purchases',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 4.2 on 2024-02-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_limited_edition_product_is_limited_edition_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['is_limited_edition'], name='idx_product_is_limited_edition'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['is_banner'], name='idx_product_is_banner'),
        ),
    ]

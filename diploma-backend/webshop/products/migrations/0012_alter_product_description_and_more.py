# Generated by Django 4.2.10 on 2024-02-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_review_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='product',
            name='full_description',
            field=models.CharField(blank=True, max_length=20000),
        ),
    ]
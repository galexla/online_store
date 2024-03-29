# Generated by Django 4.2.10 on 2024-03-14 16:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999999)])),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(1)])),
                ('paid_sum', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

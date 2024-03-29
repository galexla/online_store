# Generated by Django 4.2.10 on 2024-03-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_order_archived'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='date',
            new_name='created_at',
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['archived'], name='idx_order_archived'),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['created_at'], name='idx_review_created_at'),
        ),
    ]

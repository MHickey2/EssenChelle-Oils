# Generated by Django 3.2 on 2023-03-13 15:09

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_product_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review_date',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder1', max_length=255, verbose_name='image'),
        ),
    ]

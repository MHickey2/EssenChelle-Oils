# Generated by Django 3.2 on 2023-03-23 21:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default='v1678718256/placeholder1_r50jax.png', max_length=255, verbose_name='image'),
        ),
    ]

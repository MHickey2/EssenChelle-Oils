# Generated by Django 3.2 on 2023-03-23 20:58

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default='v1677333448/pa9lehu7vhb8pp5mvtyi.jpg', max_length=255, verbose_name='image'),
        ),
    ]

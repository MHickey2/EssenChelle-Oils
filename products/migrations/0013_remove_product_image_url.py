# Generated by Django 3.2 on 2023-02-25 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]

# Generated by Django 3.2 on 2023-02-24 19:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0010_product_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
    ]

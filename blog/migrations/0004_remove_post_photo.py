# Generated by Django 3.2 on 2023-02-19 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
    ]

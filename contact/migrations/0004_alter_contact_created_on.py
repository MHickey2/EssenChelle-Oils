# Generated by Django 3.2 on 2023-03-13 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

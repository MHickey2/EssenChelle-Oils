# Generated by Django 3.2 on 2023-02-15 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default='1'),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.TextField(verbose_name=models.CharField(default='anonymous', max_length=40)),
        ),
    ]
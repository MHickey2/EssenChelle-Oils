from django.db import models
from django.utils import timezone


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=150)
    message = models.TextField(max_length=1000)
    created_on = models.DateTimeField(default=timezone.now)

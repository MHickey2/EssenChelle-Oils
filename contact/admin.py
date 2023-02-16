from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email_address',
        'message',
        'created_on',
    )

    ordering = ('created_on',)

from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'subject',
        'email_address',
        'message',
        'created_on',
    )
    search_fields = ['last_name', 'created_on']
    list_filter = ('last_name', 'created_on')

    ordering = ('created_on',)

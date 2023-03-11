from django.contrib import admin
from .models import UserProfile
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(UserProfile)


# class PostAdmin(SummernoteModelAdmin):

#     list_display = ('user',  'profile_pic')
#     search_fields = ['user']

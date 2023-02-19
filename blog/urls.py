from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.PostList.as_view(), name='blog'),
    
]

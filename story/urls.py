from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('about', views.about, name='about'),
    path('ourproducts', views.ourproducts, name='ourproducts'),
    path('faq', views.faq, name='faq'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    path('copyright', views.copyright, name='copyright'),
]

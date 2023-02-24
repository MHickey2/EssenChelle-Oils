from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('favourite_add/<int:product_id>/', views.favourite_add, name='favourite_add'),  # noqa
    path('favourite_list/', views.favourite_list, name='favourite_list'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),  # noqa

]

from django.urls import path
from . import views
from .views import AddPostView, EditPostView

urlpatterns = [
    path('blog', views.PostList.as_view(), name='blog'),
    path('add_blog/', views.AddPostView.as_view(), name='add_blog'),
    path('<slug:slug>/', views.PostDetails.as_view(), name='post_details'),
    path('<slug:slug>/edit_blog/', views.EditPostView.as_view(), name='edit_blog'),  # noqa
    path('<slug:slug>/delete_blog/', views.DeletePostView.as_view(),
         name='delete_blog'),

]

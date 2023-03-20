from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AddPostView, EditPostView, DeletePostView, PostDetails

urlpatterns = [
    path('blog', views.PostList.as_view(), name='blog'),
    path('add_blog/', views.AddPostView.as_view(), name='add_blog'),
    path('<slug:slug>/', views.PostDetails.as_view(), name='blog_details'),
    path('edit_blog/<slug:slug>', views.EditPostView.as_view(),
         name='edit_blog'),
    path('<slug:slug>/delete_blog/', views.DeletePostView.as_view(),
         name='delete_blog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

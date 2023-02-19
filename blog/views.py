from django.shortcuts import render
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
# from cloudinary.models import CloudinaryField

# Create your views here.


# Create your views here.
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html"
    context_object_name = 'post_list'
    # paginate_by = 6
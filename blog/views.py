from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # noqa
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.urls import reverse_lazy
from cloudinary.models import CloudinaryField


# Create your views here.
class PostList(generic.ListView):
    """ users can see a selecton of blog posts promoting products on site """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html"
    context_object_name = 'post_list'
    paginate_by = 6


class PostDetails(View):
    """ allows user to a full blog post """
    def get(self, request, slug, *args, **kwargs):
        """ Presents the details of individual blogs on the Blog Detail Page """  # noqa
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        number_of_comments = post.comments.count()

        return render(
            request,
            "blog/blog_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ allows user to post comments on blogs """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()
        msg = 'Your comment was added successfully and is awaiting approval!'
        messages.add_message(self.request, messages.SUCCESS, msg)
        return render(
            request,
            "blog/blog_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
            },
        )


class AddPostView(generic.CreateView):
    """ allows a superuser to add a Blog """
    model = Post
    form_class = PostForm
    template_name = 'blog/add_blog.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        """ Ensures form valid and new inputs are saved"""
        """ adding the username automatically for the post """
        msg = 'Your Blog has been created successfully'
        messages.add_message(self.request, messages.SUCCESS, msg)
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class EditPostView(generic.UpdateView):
    """ allows a superuser to edit a Blog """
    model = Post
    form_class = PostForm
    template_name = 'blog/edit_blog.html'

    def get_success_url(self):
        slug = self.kwargs["slug"]
        msg = 'The Blog has been edited successfully'
        messages.add_message(self.request, messages.SUCCESS, msg)
        return reverse('blog')


class DeletePostView(generic.DeleteView):
    """ allows a superuser to delete a Blog """
    model = Post
    template_name = "blog/delete_blog.html"
    success_url = reverse_lazy('blog')


class LatestPostView(generic.ListView):
    """ user can see the latest 5 blog titles """
    model = Post
    latest = Post.objects.filter(status=1).order_by("-created_on")[:5]
    template_name = "blog/blog.html"
    context_object_name = 'latest'

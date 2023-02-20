from django.shortcuts import render
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # noqa
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
# from cloudinary.models import CloudinaryField


# Create your views here.
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog.html"
    context_object_name = 'post_list'
    # paginate_by = 6


class PostDetails(View):

    def get(self, request, slug, *args, **kwargs):
        """ Presents the details of individual blogs on the Blog Detail Page """  # noqa
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        # profile = Profile.objects.filter(user=post.author)[0]

        return render(
            request,
            "blog/blog_details.html",
            {
                "post": post,
            },
        )


class AddPostView(generic.CreateView):
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
    model = Post
    form_class = PostForm
    template_name = 'blog/edit_blog.html'

    def get_success_url(self):
        """ Allows the superuser to edit an existing blog """
        slug = self.kwargs["slug"]
        msg = 'The Blog has been edited successfully'
        messages.add_message(self.request, messages.SUCCESS, msg)
        return reverse("blog")


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = "blog/delete_blog.html"    

    def get_success_url(self):
        """ Allows the superuser  """        
        msg = 'The Blog has been deleted successfully'
        messages.add_message(self.request, messages.SUCCESS, msg)
        success_url = reverse_lazy('blog')

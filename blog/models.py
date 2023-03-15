# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


fs = FileSystemStorage(location='/media/photos')

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=60, unique=True, blank=False,)
    excerpt = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # noqa
    blog_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=7000)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def number_of_comments(self):
        return self.comments.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

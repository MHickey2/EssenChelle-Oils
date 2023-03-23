from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from cloudinary.models import CloudinaryField

fs = FileSystemStorage(location='/media/photos')


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)  # noqa
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # noqa
    favourites = models.ManyToManyField(User, related_name='favourites', default=None, blank=True)  # noqa
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField('image',
                            default='v1678718256/placeholder1_r50jax.png')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def number_of_reviews(self):
        return self.reviews.count()


class Review(models.Model):
    name = models.CharField(max_length=80)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")  # noqa
    rate_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    stars = models.IntegerField(choices=rate_choices, default=1)
    body = models.TextField(max_length=4000)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.name}"

    def get_absolute_url(self):
        """ Returns review with primary key"""
        return reverse('product_detail', kwargs={'pk': self.pk})

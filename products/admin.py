from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'is_featured'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', )
    search_fields = ('name', 'body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

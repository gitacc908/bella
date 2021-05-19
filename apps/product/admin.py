from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from apps.product.models import Category
from apps.product.models import Product


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'article', 'quantity', 'color',
        'price', 'description', 'fabric_structure',
        'size_range', 'length', 'fashion',
        'discount', 'rating', 'created', 'updated'
    )
    list_filter = (
        'title', 'price', 'created', 'updated',
        'discount'
    )
    search_fields = (
        'title__startswith',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

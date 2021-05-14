from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from apps.category.models import Category


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)

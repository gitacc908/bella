from django.contrib import admin

from apps.news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'draft')
    list_display_links = ('title',)
    list_filter = ('title', 'created_at')
    list_editable = ('draft',)
    prepopulated_fields = {'slug': ('title',)}

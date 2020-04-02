from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """Класс для автозаполениня slug из модели Post по полю title."""
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('author', 'title', 'text', 'published_date')
    list_filter = ('published_date',)
    list_display_links = ('author', 'title',)
    search_fields = ["title", "text"]


admin.site.register(Post, PostAdmin)

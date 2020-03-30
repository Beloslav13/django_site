from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """Класс для автозаполениня slug из модели Post по полю title."""
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)

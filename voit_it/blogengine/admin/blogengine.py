import re

from django.contrib import admin
from django import forms
from blogengine.models.posts import Post, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.
class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(), label='Детальное описание')

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    # автозаполнение slug из модели Post по полю title
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('author', 'title', 'get_clear_text', 'published_date')
    list_filter = ('published_date',)
    list_display_links = ('author', 'title',)
    search_fields = ["title", "text"]

    def get_clear_text(self, obj):
        """Получить отформатированный текст от тегов HTML."""
        return re.sub(r'(\<(/?[^>]+)>)', '', obj.text[:200])
    get_clear_text.short_description = 'Детальное описание'

    form = PostAdminForm


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')
    list_display_links = ('title', 'slug',)
    search_fields = ["title"]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

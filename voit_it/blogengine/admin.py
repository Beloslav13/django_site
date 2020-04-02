from django.contrib import admin
from django import forms
from .models import Post, Category
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
    list_display = ('author', 'title', 'text', 'published_date')
    list_filter = ('published_date',)
    list_display_links = ('author', 'title',)
    search_fields = ["title", "text"]

    form = PostAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(Category)

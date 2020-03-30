from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from easy_thumbnails.fields import ThumbnailerImageField


# Create your models here.
from django.utils import timezone


class Post(models.Model):
    """Модель поста."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Детальное описание поста')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL', blank=True)
    image = ThumbnailerImageField(upload_to='uploads', blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-published_date', 'title']

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'slug': self.slug})

    def published(self):
        """Метод публикации поста"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

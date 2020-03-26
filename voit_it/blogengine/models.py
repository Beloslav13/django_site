from django.db import models


# Create your models here.
from django.utils import timezone


class Post(models.Model):
    """Модель поста."""
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def published(self):
        """Метод публикации поста"""
        self.published_date = timezone.now()
        self.save()

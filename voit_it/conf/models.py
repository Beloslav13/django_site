from django.db import models
from django.shortcuts import reverse

from easy_thumbnails.fields import ThumbnailerImageField


# Create your models here.
class SettingsSite(models.Model):
    domain = models.CharField(max_length=150, verbose_name='Доменное имя')
    logo = ThumbnailerImageField(upload_to='uploads/logo', blank=True, verbose_name='Логотип')

    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'

    def __str__(self):
        return self.domain

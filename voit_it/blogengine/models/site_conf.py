from django.db import models
from django.contrib.sites.models import Site
from django.contrib.syndication.views import add_domain


class SiteConf(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    logo = models.FileField(verbose_name='Логотип', upload_to='uploads/logo', blank=True, null=True)

    class Meta:
        verbose_name = 'Сайт Конф'
        verbose_name_plural = 'Сайт Конф'

    def __str__(self):
        return self.id

    @property
    def url(self):
        return add_domain(self.site.domain, '')

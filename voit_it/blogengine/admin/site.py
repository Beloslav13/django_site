from django.contrib import admin
from django.contrib.sites.models import Site

from blogengine.models.site_conf import SiteConf


class ExtendSiteInline(admin.StackedInline):
    model = SiteConf
    can_delete = False


class SiteAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = (ExtendSiteInline, )


admin.site.unregister(Site)
admin.site.register(Site, SiteAdmin)

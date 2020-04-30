from django import template
from django.contrib.sites.shortcuts import get_current_site

from classytags.core import Tag, Options
from classytags.arguments import Argument

register = template.Library()


class SiteLogo(Tag):
    name = 'site_logo'

    options = Options(
        'as',
        Argument('varname', required=False, resolve=False)
    )

    def render_tag(self, context, varname):
        request = getattr(context, 'request', None)
        if not request:
            request = context.get('request')

        site = get_current_site(request)
        siteconf = getattr(site, 'siteconf', None)

        if varname:
            static_url_img = '/media/uploads/logo/logo.png'
            logo_data = {
                'logo': siteconf.logo.url if siteconf is not None and siteconf.logo else static_url_img,
                'alt': site.name
            }
            context[varname] = logo_data
            return ''
        else:
            return ''


@register.filter(name='split')
def split(value, sep):
    return value.split(sep)


register.tag(SiteLogo)

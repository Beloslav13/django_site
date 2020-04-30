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
        siteconf = site.siteconf
        if varname:
            logo_data = {
                'logo': siteconf.logo if siteconf.logo else '',
                'alt': site.name
            }
            context[varname] = logo_data
            return ''
        else:
            return ''


register.tag(SiteLogo)

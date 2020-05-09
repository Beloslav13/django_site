from django import template
from django.contrib.sites.shortcuts import get_current_site

from classytags.core import Tag, Options
from classytags.arguments import Argument

from blogengine.models.posts import Post

register = template.Library()


@register.filter(name='split')
def split(value, sep):
    return value.split(sep)


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


register.tag(SiteLogo)


class LastPosts(Tag):
    name = 'last_posts'

    options = Options(
        'as',
        Argument('varname', required=False, resolve=False)
    )

    def render_tag(self, context, varname, name=name):
        last_posts = Post.objects.all()[:3]
        if varname:
            context[varname] = last_posts
            return ''
        else:
            context[name] = last_posts
            return ''


register.tag(LastPosts)


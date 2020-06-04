from django.db.models.signals import post_save
from django.dispatch import receiver

from blogengine.models.posts import Post


# Test
@receiver(post_save, sender=Post, dispatch_uid='invalidate_post')
def invalidate_post(sender, instance, **kwargs):
    instance.author.first_name = 'Beloslav123'
    instance.author.save()

from django.shortcuts import render
from django.utils import timezone
# Create your views here.

from .models import Post


def posts_list(request):
    """Все посты"""
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blogengine/index.html', context={'posts': posts})


def post_details(request, slug):
    """Пост детально"""
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blogengine/post_details.html', context={'post': post})

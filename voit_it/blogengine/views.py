from django.shortcuts import render
from django.utils import timezone
# Create your views here.

from .models import Post, Category


def index(request):
    """Главная страница"""
    return render(request, 'index.html')


def posts_list(request):
    """Все посты"""
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'posts/posts_list.html', context={'posts': posts})


def post_details(request, slug):
    """Пост детально"""
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'posts/post_details.html', context={'post': post})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'category/categories_list.html', context={'categories': categories})


def category_detail(request, slug):
    category = Category.objects.get(slug__iexact=slug)
    return render(request, 'category/category_detail.html', context={'category': category})

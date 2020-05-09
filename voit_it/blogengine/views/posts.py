from django.shortcuts import render
from django.utils import timezone

from blogengine.models.posts import Post, Category


def index(request):
    """Главная страница"""
    return render(request, 'index.html')


def posts_list(request):
    """Все посты"""
    posts = Post.objects.filter(published_date__lte=timezone.now())
    # TODO: придумать способ получения последних постов без копипаста
    last_posts = Post.objects.all()[:3]
    return render(request, 'posts/posts_list.html', context={'posts': posts, 'last_posts': last_posts})


def post_details(request, slug):
    """Пост детально"""
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'posts/post_details.html', context={'post': post})


def categories_list(request):
    categories = Category.objects.all()
    # TODO: придумать способ получения последних постов без копипаста
    last_posts = Post.objects.all()[:3]
    return render(request, 'category/categories_list.html', context={'categories': categories, 'last_posts': last_posts})


def category_detail(request, slug):
    category = Category.objects.get(slug__iexact=slug)
    # TODO: придумать способ получения последних постов без копипаста
    last_posts = Post.objects.all()[:3]
    return render(request, 'category/category_detail.html', context={'category': category, 'last_posts': last_posts})

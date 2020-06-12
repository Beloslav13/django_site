from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets

from blogengine.models.posts import Post, Category
from blogengine.rest.serializers.post import PostSerializer


def index(request):
    """Главная страница"""
    return render(request, 'blogengine/index.html')


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published_date__lte=timezone.now())


def posts_list(request):
    """Все посты"""
    posts = Post.objects.filter(published_date__lte=timezone.now())
    paginator = Paginator(posts, 5) # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        post_paginator = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post_paginator = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post_paginator = paginator.page(paginator.num_pages)

    return render(request, 'blogengine/posts/posts_list.html', context={'posts': post_paginator})


def post_details(request, slug):
    """Пост детально"""
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blogengine/posts/post_details.html', context={'post': post})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'blogengine/category/categories_list.html', context={'categories': categories})


def category_detail(request, slug):
    category = Category.objects.get(slug__iexact=slug)
    return render(request, 'blogengine/category/category_detail.html', context={'category': category})

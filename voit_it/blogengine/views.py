from django.shortcuts import render


# Create your views here.
from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blogengine/index.html', context={'posts': posts})

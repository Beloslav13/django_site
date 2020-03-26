from django.shortcuts import render
from django.utils import timezone
# Create your views here.

from .models import Post


def posts_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'blogengine/index.html', context={'posts': posts})

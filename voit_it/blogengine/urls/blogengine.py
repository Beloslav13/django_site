from django.urls import path

from blogengine.views.posts import post_details, index, categories_list, category_detail, posts_list

urlpatterns = [
    path('', index, name='index'),
    path('reading/', posts_list, name='posts_list'),
    path('post/<str:slug>/', post_details, name='post_details'),
    path('categories/', categories_list, name='categories_list'),
    path('categories/<str:slug>/', category_detail, name='category_detail')
]


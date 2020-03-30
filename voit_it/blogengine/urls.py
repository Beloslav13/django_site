from django.urls import path

from .views import posts_list, post_details, index

urlpatterns = [
    path('', index, name='index'),
    path('reading', posts_list, name='posts_list'),
    path('post/<str:slug>/', post_details, name='post_details')
]
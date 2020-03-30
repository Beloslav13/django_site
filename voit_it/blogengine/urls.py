from django.urls import path

from .views import posts_list, post_details

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('post/<str:slug>/', post_details, name='post_details')
]
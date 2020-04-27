from django.urls import path, include

from .views import rend_logo

urlpatterns = [
    path('', rend_logo, name='rend_logo'),

]
from django.urls import include, path
from rest_framework import routers

from blogengine.models.posts import Post
from blogengine.views import customer, posts

router = routers.DefaultRouter()
router.register(r'users', customer.UserViewSet)
router.register(r'groups', customer.GroupViewSet)
router.register(r'posts', posts.PostViewSet, basename=Post)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


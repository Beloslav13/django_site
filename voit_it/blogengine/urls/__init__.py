from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogengine.urls.blogengine')),
    path('new/', TemplateView.as_view(template_name='new.html'), name='new'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/', include('blogengine.urls.rest_api')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
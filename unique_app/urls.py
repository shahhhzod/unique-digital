from django.urls import path
from .views import blog_index, post_detail, inquiry_view
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('blog/', blog_index, name='blog_index'),
    path('blog/<int:pk>/', post_detail, name='post_detail'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('inquiry/', inquiry_view, name='inquiry'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

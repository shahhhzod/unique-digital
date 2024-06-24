from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from unique_app.views import blog_index, post_detail, home, services, post_list_by_category, inquiry_view, web_development, smm_services, seo_services, design_services, portfolio_list,  portfolio_detail, success_view, web_analytics, calculator_web, targeting_page, set_language

urlpatterns = [
    path('', home, name='home'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('portfolio/', portfolio_list, name='portfolio-list'),
    path('services/', services, name='services'),
    path('services/web-development/', web_development, name='web-development'),
    path('services/smm/', smm_services, name='smm-services'),
    path('services/calculator-web/', calculator_web, name='calculator-web'),
    path('services/seo/', seo_services, name='seo-services'),
    path('services/design/', design_services, name='design-services'),
    path('services/web-analytics', web_analytics, name='web-analytics'),
    path('services/targeting',  targeting_page, name='targeting-page'),
    path('admin/', admin.site.urls),
    path('portfolio/<int:pk>/', portfolio_detail, name='portfolio-detail'),
    path('blog/', blog_index, name='blog_index'),
    path('category/<slug:category_slug>/', post_list_by_category, name='post_list_by_category'),
    path('blog/<int:pk>/', post_detail, name='post_detail'),
    path('inquiry/', inquiry_view, name='inquiry'),
    path('success/', success_view, name='success_url'),  # Убедитесь, что имя URL соответствует
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # Third-party apps
    path('rest-auth/', include('rest_framework.urls')),

    # Local apps
    path('api1/', include('apps.users.urls')),
    path('api2/', include('apps.category.urls')),
    path('api4/', include('apps.order.urls')),
    path('api5/', include('apps.product.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

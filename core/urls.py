from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from apps.users.views import BlackListTokenView


urlpatterns = [
    path('admin/', admin.site.urls),

    # Third-party apps
    path('rest-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), 
        name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), 
        name='token-refresh'),
    path('token/logout/blacklist/', BlackListTokenView.as_view(),
        name='blacklist'),

    # Local apps
    path('api1/', include('apps.users.urls')),
    path('api2/', include('apps.product.urls')),
    path('api3/', include('apps.order.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

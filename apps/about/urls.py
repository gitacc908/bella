from django.urls import path
from .views import AboutAPIView


urlpatterns = [
    path('about-info/', AboutAPIView.as_view(),
         name='about-info'),
]

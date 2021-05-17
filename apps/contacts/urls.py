from django.urls import path
from .views import ContactAPIView


urlpatterns = [
    path('contact-info/', ContactAPIView.as_view(),
         name='contact-info'),
]

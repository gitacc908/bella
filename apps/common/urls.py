from django.urls import path

from .views import (
    DeliveryAPIView, ContactAPIView, AboutAPIView, FAQAPIView,
    NewsAPIView
)


urlpatterns = [
    path('about-info/', AboutAPIView.as_view(),
         name='about-info'),
    path('contact-info/', ContactAPIView.as_view(),
         name='contact-info'),
    path('delivery-info/', DeliveryAPIView.as_view(),
         name='delivery-info'),
    path('faq-info/', FAQAPIView.as_view(),
         name='faq-info'),
    path('news-info/', NewsAPIView.as_view(),
         name='news-info'),
]

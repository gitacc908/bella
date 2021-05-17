from django.urls import path
from .views import FAQAPIView


urlpatterns = [
    path('faq-info/', FAQAPIView.as_view(),
         name='faq-info'),
]

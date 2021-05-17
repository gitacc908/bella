from django.urls import path
from .views import NewsAPIView


urlpatterns = [
    path('news-info/', NewsAPIView.as_view(),
         name='news-info'),
]

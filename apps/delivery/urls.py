from django.urls import path
from .views import DeliveryAPIView


urlpatterns = [
    path('delivery-info/', DeliveryAPIView.as_view(),
         name='delivery-info'),
]

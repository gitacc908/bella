from django.urls import path

from apps.order.views import OrderAPICreateView

urlpatterns = [
    path('order-create/', OrderAPICreateView.as_view(), name='order-create'),
]

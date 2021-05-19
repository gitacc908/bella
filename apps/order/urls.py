from django.urls import path

# from apps.order.views import OrderAPICreateView
from apps.order.views import CreateOrderAPIView

urlpatterns = [
    # path('order-create/', OrderAPICreateView.as_view(),
    #     name='order-create'),
    path('order-create/', CreateOrderAPIView.as_view(),
         name='order-create')
]

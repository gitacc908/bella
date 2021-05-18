from rest_framework import generics, permissions

from apps.order.models import Order, OrderItem
from apps.order.serializers import OrderSerializer, OrderItemSerializer
from apps.product.models import Product

# TODO: We will get data from FrontEnd after front part will send to us this data 

# class OrderAPICreateView(generics.CreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#     def perform_create(self, serializer):
        
#         order = serializer.save(owner=self.request.user)
#         product = SomeProductHereFromFrontEnd'sRequest
#         OrderItem.objects.create(
#             owner=self.request.user,
#             order=order,
#             product=product,
#             price=150,
#             quantity=2
#         )
#         return super().perform_create(serializer)

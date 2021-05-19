from rest_framework import generics, permissions
from rest_framework.views import APIView
from apps.order.models import Order, OrderItem
from apps.order.serializers import OrderSerializer, OrderItemSerializer
from apps.product.models import Product
from rest_framework.response import Response


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


# TODO: later will rewrite with generic view and mb update logic:)
class CreateOrderAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        given_ids = [4, 5, 6]  # product ids from front
        order, _ = Order.objects.get_or_create(owner=request.user)
        products = Product.objects.filter(pk__in=given_ids)
        order_items = OrderItem.objects.bulk_create(
            [
                OrderItem(
                    owner=request.user, product=item,
                    price=item.price, order=order
                ) for item in products
            ]
        )
        return Response(order_items)

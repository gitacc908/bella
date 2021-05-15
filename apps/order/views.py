from rest_framework import generics

from apps.order.models import Order, OrderItem
from apps.order.serializers import OrderSerializer, OrderItemSerializer
from apps.product.models import Product


class OrderAPICreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # Note: Adilet is responsible to Cart and Product parts. That's why I used my own data to test this view.
        if self.request.user.is_authenticated:
            order = serializer.save(owner=self.request.user)
            product = Product.objects.first()
            OrderItem.objects.create(
                owner=self.request.user,
                order=order,
                product=product,
                price=150,
                quantity=2
            )
        else:
            order = serializer.save()
            product = Product.objects.first()
            OrderItem.objects.create(
                order=order,
                product=product,
                price=150,
                quantity=2
            )
        return super().perform_create(serializer)

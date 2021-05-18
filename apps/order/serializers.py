from rest_framework import serializers

from apps.order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'owner', 'order', 'product', 'price', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'owner', 'is_paid', 'buying_type', 'is_delivered')

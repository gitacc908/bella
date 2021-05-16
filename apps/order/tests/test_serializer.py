import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.category.models import Category
from apps.order.choices import CASH
from apps.order.models import Order, OrderItem
from apps.order.serializers import OrderSerializer, OrderItemSerializer
from apps.product.models import Product

User = get_user_model()


class OrderAPITestCase(TestCase):
    def test_serializer(self) -> None:
        self.user = User.objects.create_user(
            phone='+996776005776',
            first_name='test user',
            last_name='test lastname',
            password='password123'
        )
        self.category = Category.objects.create(
            title='test parent',
            slug='test-parent',
        )
        self.product = Product.objects.create(
            title='test product'
        )
        self.product.category.set((self.category,))
        url = reverse('order-create')
        data = {
            'buying_type': CASH
        }
        json_data = json.dumps(data)
        self.client.post(url, data=json_data,
                         content_type='application/json')
        order = Order.objects.first()
        order_item = OrderItem.objects.first()
        serializer_data_order = OrderSerializer(order).data
        serializer_data_order_item = OrderItemSerializer(order_item).data
        expected_data_order = {
            'id': order.id,
            'owner': None,
            'is_paid': False,
            'buying_type': 1,
            'is_delivered': False
        }
        expected_data_order_item = {
            'id': order_item.id,
            'owner': None,
            'order': 6,
            'product': 9,
            'price': '150.00',
            'quantity': 2
        }
        self.assertEqual(expected_data_order, serializer_data_order)
        self.assertEqual(expected_data_order_item, serializer_data_order_item)

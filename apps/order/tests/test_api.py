import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from apps.category.models import Category
from apps.order.choices import CASH
from apps.order.models import Order, OrderItem
from apps.product.models import Product


User = get_user_model()


class OrderAPITestCase(TestCase):
    def setUp(self) -> None:
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

    def test_order_create_without_user(self):
        """
        Order and Order Item API creat test without user
        """
        orders_before_creating = Order.objects.all().count()
        url = reverse('order-create')
        data = {
            'buying_type': CASH
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')
        order = Order.objects.first()
        expected_data = f'Заказ для {self.product.title} продукта от анонимного пользователя'
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(self.product, order.order_items.all()[0].product)
        self.assertEqual(expected_data, str(order.order_items.all()[0]))
        self.assertEqual(CASH, order.buying_type)
        self.assertNotEqual(1, orders_before_creating)

    def test_order_create_with_user(self):
        """
        Order and Order Item API creat test with user
        """
        orders_before_creating = Order.objects.all().count()
        url = reverse('order-create')
        data = {
            'buying_type': CASH
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')
        order = Order.objects.first()
        expected_data = f'Заказ для {self.product.title} продукта \
                        от {self.user.first_name} {self.user.last_name}'
        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)
        self.assertEqual(self.product, order.order_items.all()[0].product)
        self.assertEqual(expected_data, str(order.order_items.all()[0]))
        self.assertEqual(self.user, order.owner)
        self.assertEqual(CASH, order.buying_type)
        self.assertNotEqual(1, orders_before_creating)

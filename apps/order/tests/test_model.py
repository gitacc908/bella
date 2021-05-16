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
        self.order = Order.objects.create(
            owner=self.user,
            buying_type=CASH
        )
        OrderItem.objects.create(
            owner=self.user,
            order=self.order,
            product=self.product,
            price=150,
            quantity=2
        )

    def test_order_created(self):
        order = Order.objects.first()
        self.assertEqual(self.user, order.owner)
        self.assertEqual(CASH, order.buying_type)
        self.assertFalse(order.is_paid)
        self.assertFalse(order.is_delivered)

    def test_order_item_created(self):
        order_item = OrderItem.objects.first()
        self.assertEqual(self.user, order_item.owner)
        self.assertEqual(self.order, order_item.order)
        self.assertEqual(self.product, order_item.product)
        self.assertEqual(150, order_item.price)
        self.assertEqual(2, order_item.quantity)

    def test_order_item_get_cost_method(self):
        self.assertEqual(300, OrderItem.objects.first().get_cost())

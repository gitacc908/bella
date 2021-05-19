from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.product.models import Category
from apps.product.models import Product
from apps.users.models import Bookmark

User = get_user_model()


class CustomUserTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            phone="+996777777777",
            first_name="User123",
            last_name="Userevich",
            password="Testpass123"
        )
        User.objects.create_superuser(
            phone="+996776005776",
            password="Testpass123"
        )
        cls.user = User.objects.first()
        cls.admin_user = User.objects.last()

    def test_user_created(self):
        self.assertEqual("+996777777777", self.user.phone)
        self.assertEqual("User123", self.user.first_name)
        self.assertEqual("Userevich", self.user.last_name)
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_superuser_created(self):
        self.assertEqual("+996776005776", self.admin_user.phone)
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)

    def test_user_phone_number(self):
        phone_label = self.user._meta.get_field('phone').verbose_name
        self.assertEqual('Номер телефона', phone_label)

    def test_favorite_products(self):
        category1 = Category.objects.create(
            title='test parent',
            slug='test-parent',
        )
        product = Product.objects.create(
            title='test product'
        )
        product.category.set((category1,))
        self.user.product.set((product,))
        self.assertEqual(product, self.user.product.all()[0])
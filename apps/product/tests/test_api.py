from django.test import TestCase
from rest_framework import status

from apps.product.models import Category
from apps.product.models import Product
from apps.product.choices import AMPIR
from django.urls import reverse

from apps.product.serializers import (
    CategorySerializer, CategoryDetailSerializer,
    ProductSerializer
)


class CategoryAPITestCase(TestCase):
    def setUp(self) -> None:
        Category.objects.create(
            title='test parent',
            slug='test-parent',
        )
        Category.objects.create(
            title='test children',
            slug='test-children',
            parent=Category.objects.first()
        )
        product = Product.objects.create(
            title='test product',
            article='some article',
            quantity=20,
            price=123,
            description='some desc',
            fashion=AMPIR,
            discount=10,
        )
        product.categories.set((Category.objects.last(),))

    def test_get(self):
        url = reverse('category-list')
        response = self.client.get(url)
        categories = Category.objects.filter(parent=None)
        serializer_data = CategorySerializer(categories, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(1, len(response.data))

    def test_get_detail(self):
        url = reverse('category-detail', args=(Category.objects.last().slug, ))
        response = self.client.get(url)
        category = Category.objects.last()
        serializer_data = CategoryDetailSerializer(category).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class ProductAPITestCase(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(
            title='test category',
            slug='test-slug',
        )
        self.product = Product.objects.create(
            title='test product',
            article='some article',
            quantity=20,
            price=123,
            description='some desc',
            fashion=AMPIR,
            discount=10,
        )
        self.product2 = Product.objects.create(
            title='test product2',
            article='some article2',
            quantity=20,
            price=123,
            description='some desc2',
            fashion=AMPIR,
            discount=10,
        )
        self.product.categories.add(self.category)
        self.product2.categories.add(self.category)
        self.product2.categories.remove(self.category)

    def test_get_all(self):
        response = self.client.get(reverse('product-list'))
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True).data
        self.assertEqual(product_serializer, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        response = self.client.get(
            reverse('product-detail', kwargs={"slug": self.product.slug})
        )
        product_serializer = ProductSerializer(self.product).data
        self.assertEqual(product_serializer, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn(self.category, self.product.categories.all())
        self.assertNotIn(self.category, self.product2.categories.all())

    def test_best_seller(self):
        response = self.client.get(reverse('best-seller'))
        bs_queryset = Product.objects.order_by('-rating')[0:12]
        product_serializer = ProductSerializer(bs_queryset, many=True).data
        self.assertEqual(product_serializer, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

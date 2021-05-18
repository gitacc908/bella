from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from apps.product.models import Category
from apps.product.serializers import CategorySerializer, CategoryDetailSerializer
from apps.product.models import Product


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
            title='test product'
        )
        product.category.set((Category.objects.last(),))

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

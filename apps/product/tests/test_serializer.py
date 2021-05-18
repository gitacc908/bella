from django.test import TestCase

from apps.product.models import Category
from apps.product.serializers import CategorySerializer, CategoryDetailSerializer
from apps.product.models import Product


class CategorySerializerTestCase(TestCase):

    def test_serializer(self):
        category1 = Category.objects.create(
            title='test parent',
            slug='test-parent',
        )
        category2 = Category.objects.create(
            title='test children',
            slug='test-children',
            parent=Category.objects.first()
        )
        product = Product.objects.create(
            title='test product'
        )
        product.category.set((category2,))
        categories = Category.objects.filter(parent=None)
        serializer_data = CategorySerializer(categories, many=True).data
        expected_data = [
            {
                'id': category1.id,
                'title': 'test parent',
                'slug': 'test-parent',
                'children': [
                    {
                        'id': category2.id,
                        'title': 'test children',
                        'slug': 'test-children',
                        'children': []
                    }
                ]
            }
        ]
        serializer_data_detail = CategoryDetailSerializer(category2).data
        expected_data_detail = {
                'id': category2.id,
                'title': 'test children',
                'products': [
                    product.id
                ]
            }
        self.assertEqual(expected_data, serializer_data)
        self.assertEqual(expected_data_detail, serializer_data_detail)

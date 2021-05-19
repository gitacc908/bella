from django.test import TestCase

from apps.product.models import Category
from apps.product.models import Product
from apps.product.serializers import (
    CategorySerializer, CategoryDetailSerializer, ProductSerializer
)
from apps.product.choices import (
    AMPIR, POLYESTER, XL, CYAN
)


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
            title='test product',
            article='some article',
            quantity=20,
            price=123,
            description='some desc',
            fashion=AMPIR,
            discount=10,
        )
        product.categories.set((category2,))
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


class ProductSerializerTestCase(TestCase):

    def test_serializer(self):
        category = Category.objects.create(
            title='test',
            slug='test',
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
        product.categories.add(category)
        serializer_data = ProductSerializer(product).data
        expected_data = {
            'id': product.id,
            'title': 'test product',
            'slug': product.slug,
            'article': 'some article',
            'quantity': 20,
            'color': CYAN,
            'price': format(123, '.2f'),
            'description': 'some desc',
            'fabric_structure': POLYESTER,
            'size_range': XL,
            'length': XL,
            'fashion': AMPIR,
            'discount': 10,
            'rating': 0,
            'categories': [category.id]
        }
        self.assertEqual(expected_data, serializer_data)
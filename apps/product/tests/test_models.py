from django.test import TestCase
from django.urls import reverse

from apps.product.choices import AMPIR
from apps.product.models import Product


class ProductModelTestCase(TestCase):
    def setUp(self) -> None:
        Product.objects.create(
            title='test product',
            article='some article',
            quantity=20,
            price=123,
            description='some desc',
            fashion=AMPIR,
            discount=10,
        )

    def test_product_created(self):
        product = Product.objects.first()
        self.assertEqual(AMPIR, product.fashion)
        self.assertEqual('some desc', product.description)
        self.assertFalse(product.rating)

    def test_product_get_absolute_url(self):
        product = Product.objects.first()
        response = self.client.get(
            reverse("product-detail", kwargs={"slug": product.slug})
        )
        self.assertEqual(200, response.status_code)

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from apps.product.choices import AMPIR
from apps.product.models import Product
from django.urls import reverse
from faker import Faker
from django.contrib.auth import get_user_model

from apps.users.serializers import (
    UserBookmarkSerializer
)

User = get_user_model()


class UsersApiTest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        fake = Faker()
        password = fake.password()
        self.user_data = {
            'phone': '+996703914165',
            'first_name': fake.name().split(' ')[0],
            'last_name': fake.name().split(' ')[1],
            'password': password,
            'password2': password
        }
        # sign up
        sent_code = '123456'
        typed_code = '123456'
        self.url_sign_up = f'http://localhost:8000/api1/sign-up/?typed_code={typed_code}&sent_code={sent_code}'
        self.resp_sign_up = self.client.post(
            self.url_sign_up, self.user_data, format='json'
        )
        # get token
        url_token = f'http://localhost:8000/token/'
        user_login = {'phone': self.user_data['phone'],
                      'password': self.user_data['password']}
        self.resp_token = self.client.post(url_token, user_login)
        self.token = self.resp_token.data['access']
        # products
        self.all_products = Product.objects.bulk_create([
            Product(
                title='test product',
                slug=str(number)+'slug',
                article='some article',
                quantity=20,
                price=123,
                description='some desc',
                fashion=AMPIR,
                discount=10
            ) for number in range(2)
        ])
        # favorite products
        self.products = {'favorite_products':
                         [product.id for product in self.all_products]
                         }

    def test_user_created(self):
        self.assertEqual(self.resp_sign_up.data['phone'],
                         self.user_data['phone'])
        self.assertEqual(self.resp_sign_up.data['first_name'],
                         self.user_data['first_name'])
        self.assertEqual(self.resp_sign_up.data['last_name'],
                         self.user_data['last_name'])
        self.assertEqual(self.resp_sign_up.status_code,
                         201)

    def test_get_token(self):
        self.assertEqual(self.resp_token.status_code, 200)

    def test_user_bookmark_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(reverse('user-bookmark'))
        user = User.objects.get(phone=self.user_data['phone'])
        user_bookmark_serializer = UserBookmarkSerializer(user).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(user_bookmark_serializer, response.data)

    def test_add_to_bookmark(self):
        user = User.objects.get(phone=self.user_data['phone'])
        product = Product.objects.last()
        self.assertNotIn(product, user.favorite_products.all())
        favorite_products = {"favorite_products": [product.id]}
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.put(reverse('bookmark-add'), favorite_products)
        user_bookmark_serializer = UserBookmarkSerializer(user).data
        self.assertEqual(user_bookmark_serializer, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn(product, user.favorite_products.all())

    def test_delete_from_bookmark(self):
        user = User.objects.get(phone=self.user_data['phone'])
        product = Product.objects.last()
        favorite_products = {"favorite_products": [product.id]}
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.client.put(reverse('bookmark-add'), favorite_products)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.put(
            reverse('bookmark-delete'), favorite_products
        )
        user_bookmark_serializer = UserBookmarkSerializer(user).data
        self.assertEqual(user_bookmark_serializer, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

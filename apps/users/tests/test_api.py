from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from apps.product.choices import AMPIR
from django.urls import reverse
from faker import Faker
from django.contrib.auth import get_user_model
from apps.users.serializers import (
    UserBookmarkSerializer, UserSerializer,
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
        user = User.objects.get(phone=self.user_data['phone'])
        token = self.resp_token.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(
            'http://localhost:8000/api1/bookmark/',
            headers={'Authorization': 'Bearer ' + token}
        )
        user_bookmark_serializer = UserBookmarkSerializer(user).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(user_bookmark_serializer, response.data)

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from apps.common.serializers import (
    AboutInfoSerializer, ContactInfoSerializer,
    DeliveryInfoSerializer, FAQSerializer, NewsSerializer
)
from apps.common.models import (
    About, Contact, DeliveryInfo, FAQ, News
)


class CommonAPPAPITestCase(TestCase):
    def setUp(self) -> None:
        About.objects.create(
            body='test body',
        )
        Contact.objects.create(
            phone_number='test phone',
            email='test email',
            location='test location'
        )
        DeliveryInfo.objects.create(
            body='test body'
        )
        FAQ.objects.create(
            question='test question',
            answer='test answer'
        )
        News.objects.create(
            title='test title',
            slug='test slug',
            body='test body'
        )

    def test_get_last(self):
        # get responce
        response_for_about = self.client.get(reverse('about-info'))
        response_for_contact = self.client.get(reverse('contact-info'))
        response_for_delivery = self.client.get(reverse('delivery-info'))
        response_for_faq = self.client.get(reverse('faq-info'))
        response_for_news = self.client.get(reverse('news-info'))

        # get objects
        about = About.objects.all()
        contact = Contact.objects.all()
        delivery = DeliveryInfo.objects.all()
        faq = FAQ.objects.all()
        news = News.objects.all()

        # serialize data
        serializer_data_about = AboutInfoSerializer(
            about, many=True).data
        serializer_data_contact = ContactInfoSerializer(
            contact, many=True).data
        serializer_data_delivery = DeliveryInfoSerializer(
            delivery, many=True).data
        serializer_data_faq = FAQSerializer(
            faq, many=True).data
        serializer_data_news = NewsSerializer(
            news, many=True).data

        # check data
        self.assertEqual(status.HTTP_200_OK, response_for_about.status_code)
        self.assertEqual(serializer_data_about, response_for_about.data)
        self.assertEqual(status.HTTP_200_OK, response_for_contact.status_code)
        self.assertEqual(serializer_data_contact, response_for_contact.data)
        self.assertEqual(status.HTTP_200_OK, response_for_delivery.status_code)
        self.assertEqual(serializer_data_delivery, response_for_delivery.data)
        self.assertEqual(status.HTTP_200_OK, response_for_faq.status_code)
        self.assertEqual(serializer_data_faq, response_for_faq.data)
        self.assertEqual(status.HTTP_200_OK, response_for_news.status_code)
        self.assertEqual(serializer_data_news, response_for_news.data)

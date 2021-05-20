from django.test import TestCase

from apps.common.models import (
    About, Contact, DeliveryInfo, FAQ, News
)
from apps.common.serializers import (
    AboutInfoSerializer, ContactInfoSerializer, DeliveryInfoSerializer,
    FAQSerializer, NewsSerializer
)


class CommonAPPSerializerTestCase(TestCase):

    def test_serializer(self):
        # setup data
        about = About.objects.create(
            body='test body'
        )
        contact = Contact.objects.create(
            phone_number='test phone',
            email='test email',
            location='test location'
        )
        delivery = DeliveryInfo.objects.create(
            body='test body'
        )
        faq = FAQ.objects.create(
            question='test question',
            answer='test answer'
        )
        news = News.objects.create(
            title='test title',
            slug='test slug',
            body='test body',
        )

        # json setup
        expected_data_about = {
            'id': about.id,
            'body': 'test body'
        }
        expected_data_contact = {
            'id': contact.id,
            'phone_number': 'test phone',
            'email': 'test email',
            'location': 'test location'
        }
        expected_data_delivery = {
            'id': delivery.id,
            'body': 'test body'
        }
        expected_data_faq = {
            'id': faq.id,
            'question': 'test question',
            'answer': 'test answer'
        }
        expected_data_news = {
            'id': news.id,
            'title': 'test title',
            'slug': 'test slug',
            'body': 'test body',
            'draft': False,
            'created_at': str(news.created_at),
            'image': None
        }

        # serialize data
        serializer_data_about = AboutInfoSerializer(about).data
        serializer_data_contact = ContactInfoSerializer(contact).data
        serializer_data_delivery = DeliveryInfoSerializer(delivery).data
        serializer_data_faq = FAQSerializer(faq).data
        serializer_data_news = NewsSerializer(news).data

        # check with imitated data
        self.assertEqual(expected_data_about, serializer_data_about)
        self.assertEqual(expected_data_contact, serializer_data_contact)
        self.assertEqual(expected_data_delivery, serializer_data_delivery)
        self.assertEqual(expected_data_faq, serializer_data_faq)
        self.assertEqual(expected_data_news, serializer_data_news)

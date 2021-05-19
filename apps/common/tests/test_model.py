from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.common.models import (
    About, Contact, DeliveryInfo, FAQ, News
)


class CommonAPPModelsTestCase(TestCase):
    def setUp(self) -> None:
        self.about = About.objects.create(
            body='test body'
        )
        self.contact = Contact.objects.create(
            phone_number='test phone',
            email='test email',
            location='test location'
        )
        self.delivery = DeliveryInfo.objects.create(
            body='test body'
        )
        self.faq = FAQ.objects.create(
            question='test question',
            answer='test answer'
        )
        self.news = News.objects.create(
            title='test title',
            slug='test slug',
            body='test body',
            image=SimpleUploadedFile(
                "news_image.jpg", content=b'', content_type="image/jpg"
            )
        )

    def test_models_created(self):
        # get single object
        about = About.objects.first()
        contact = Contact.objects.first()
        delivery = DeliveryInfo.objects.first()
        faq = FAQ.objects.first()
        news = News.objects.first()

        # for about model
        self.assertEqual(self.about, about)
        self.assertEqual(self.about.body, about.body)

        # for contact model
        self.assertEqual(self.contact, contact)
        self.assertEqual(self.contact.phone_number, contact.phone_number)
        self.assertEqual(self.contact.email, contact.email)
        self.assertEqual(self.contact.location, contact.location)

        # for contact delivery model
        self.assertEqual(self.delivery, delivery)
        self.assertEqual(self.delivery.body, delivery.body)
        self.assertTrue(self.delivery.created_at)

        # for contact faq model
        self.assertEqual(self.faq, faq)
        self.assertEqual(self.faq.question, faq.question)
        self.assertEqual(self.faq.answer, faq.answer)

        # for contact faq model
        self.assertEqual(self.news, news)
        self.assertEqual(self.news.title, news.title)
        self.assertEqual(self.news.slug, news.slug)
        self.assertEqual(self.news.body, news.body)
        self.assertFalse(self.news.draft)
        self.assertTrue(self.news.created_at)

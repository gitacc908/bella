from rest_framework import fields, serializers
from .models import (
    News, FAQ, Contact, DeliveryInfo, About
)


class AboutInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        exclude = ('created_at',)


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'phone_number', 'email', 'location')


class DeliveryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryInfo
        exclude = ('created_at',)


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'question', 'answer')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'slug', 'body', 'draft',
                  'created_at', 'image')

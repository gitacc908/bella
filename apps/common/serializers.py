from rest_framework import serializers
from .models import (
    News, FAQ, Contact, DeliveryInfo, About
)


class AboutInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        exclude = ('id', 'created_at')


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ('id',)


class DeliveryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryInfo
        exclude = ('id', 'created_at')


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        exclude = ('id',)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ('slug', 'id')

from rest_framework import fields, serializers
from .models import (
    News, FAQ, Contact, DeliveryInfo, About
)


class AboutInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        exclude = ('created_at')


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class DeliveryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryInfo
        exclude = ('created_at')


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

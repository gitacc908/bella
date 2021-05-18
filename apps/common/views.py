from rest_framework import generics

from .models import (
    News, FAQ, DeliveryInfo, Contact, About
)
from .serializers import (
    NewsSerializer, FAQSerializer, DeliveryInfoSerializer,
    ContactInfoSerializer, AboutInfoSerializer
)


class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutInfoSerializer


class ContactAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactInfoSerializer


class DeliveryAPIView(generics.ListAPIView):
    queryset = DeliveryInfo.objects.all()
    serializer_class = DeliveryInfoSerializer


class FAQAPIView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class NewsAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

from rest_framework import generics
from .models import Contact
from .serializers import ContactInfoSerializer


class ContactAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactInfoSerializer

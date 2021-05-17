from rest_framework import serializers
from .models import Contact


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ('id',)

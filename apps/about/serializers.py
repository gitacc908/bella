from rest_framework import serializers
from .models import About


class AboutInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        exclude = ('id', 'created_at')

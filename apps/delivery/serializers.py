from rest_framework import serializers
from .models import DeliveryInfo


class DeliveryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryInfo
        exclude = ('id', 'created_at')

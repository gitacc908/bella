from rest_framework import generics
from .models import DeliveryInfo
from .serializers import DeliveryInfoSerializer


class DeliveryAPIView(generics.ListAPIView):
    queryset = DeliveryInfo.objects.all()
    serializer_class = DeliveryInfoSerializer

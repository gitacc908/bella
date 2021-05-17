from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer


class FAQAPIView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

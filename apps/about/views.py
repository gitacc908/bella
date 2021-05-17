from rest_framework import generics
from .models import About
from .serializers import AboutInfoSerializer


class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutInfoSerializer

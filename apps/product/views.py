from rest_framework import generics
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class LatestAPIView(generics.ListAPIView):
    queryset = Product.objects.all()[0:12]
    serializer_class = ProductSerializer


class BestsellerAPIView(generics.ListAPIView):
    queryset = Product.objects.order_by('-rating')[0:12]
    serializer_class = ProductSerializer


class SortByAPIView(generics.ListAPIView):  # TODO: get sort by param from front
    # queryset = Product.objects.order_by('-rating')[0:12]
    # serializer_class = ProductSerializer
    pass

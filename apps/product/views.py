from rest_framework import generics
from apps.product.models import Product, Category
from apps.product.serializers import ProductSerializer, CategorySerializer, CategoryDetailSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'


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

from rest_framework import generics
<<<<<<< HEAD
from apps.product.models import Product, Category
from apps.product.serializers import ProductSerializer, CategorySerializer, CategoryDetailSerializer
=======

from apps.product.models import Category
from apps.product.serializers import CategorySerializer, CategoryDetailSerializer
>>>>>>> 1d4dc74c7944942684d31b4cf8ae74abd138dbd6


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'
<<<<<<< HEAD


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
=======
>>>>>>> 1d4dc74c7944942684d31b4cf8ae74abd138dbd6

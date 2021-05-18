<<<<<<< HEAD
from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('id', 'created')
=======
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from apps.product.models import Category
>>>>>>> 1d4dc74c7944942684d31b4cf8ae74abd138dbd6


class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'children')


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'products')

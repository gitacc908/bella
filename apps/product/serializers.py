from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'children')


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'products')
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True,)

    class Meta:
        model = Product
        exclude = ('created', 'updated')

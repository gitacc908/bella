from .models import Product, Category
from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('created',)


class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ('title', 'slug', 'children')


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'products')

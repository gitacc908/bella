from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from apps.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'children')


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'products')

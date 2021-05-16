from rest_framework import serializers

from apps.product.models import Product
from apps.users.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('product',)
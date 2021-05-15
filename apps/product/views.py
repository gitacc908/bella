from apps.users.models import CustomUser
from apps.product.models import Product
from rest_framework import viewsets
from apps.product.serializers import ProductSerializers


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

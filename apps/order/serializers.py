from rest_framework import serializers


class OrderSerializer(serializers.Serializer):
    product_ids = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity = serializers.IntegerField()
    buying_type = serializers.CharField()

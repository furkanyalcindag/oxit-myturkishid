from rest_framework import serializers


class CartSerializer(serializers.Serializer):
    product_id = serializers.CharField()
    quantity = serializers.CharField()

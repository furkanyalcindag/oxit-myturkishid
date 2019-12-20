from rest_framework import serializers


class SponsorApproveSerializer(serializers.Serializer):
    situation = serializers.BooleanField()


class OrderMemberSerializer(serializers.Serializer):
    district = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()


class OrderProductSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    quantity = serializers.CharField()

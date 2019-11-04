from rest_framework import serializers


class SponsorApproveSerializer(serializers.Serializer):
    situation = serializers.BooleanField()

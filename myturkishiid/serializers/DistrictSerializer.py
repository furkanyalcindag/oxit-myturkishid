from rest_framework import serializers

from myturkishiid.models.District import District


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'
        depth = 3

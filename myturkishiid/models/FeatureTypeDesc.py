from django.db import models

from myturkishiid.models import FeatureType, Language


class FeatureTypeDesc(models.Model):
    featureType = models.ForeignKey('FeatureType', on_delete=models.CASCADE)
    lang = models.ForeignKey('Language', on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True)

from django.db import models

from myturkishiid.models import FeatureType


class Feature(models.Model):
    key = models.CharField(null=True, blank=True, max_length=256)
    featureType = models.ForeignKey('FeatureType', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s ' % self.key

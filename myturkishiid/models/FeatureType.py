from django.db import models


class FeatureType(models.Model):
    key = models.CharField(null=True, blank=True, max_length=256)



    def __str__(self):
        return '%s ' % self.key

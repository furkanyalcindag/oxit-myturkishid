from django.db import models

from myturkishiid.models import Feature, Language


class FeatureDesc(models.Model):
    feature = models.ForeignKey('Feature', on_delete=models.CASCADE)
    lang = models.ForeignKey('Language', on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True, verbose_name='Özellik Adı')


    def __str__(self):
        return '%s ' % self.name

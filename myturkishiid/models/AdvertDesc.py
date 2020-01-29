from django.db import models

from myturkishiid.models import Advert, Language


class AdvertDesc(models.Model):
    advert = models.ForeignKey('Advert', on_delete=models.CASCADE)
    lang = models.ForeignKey('Language', on_delete=models.CASCADE)
    advertTitle = models.CharField(max_length=256, null=True, blank=True, verbose_name='Çeviri')

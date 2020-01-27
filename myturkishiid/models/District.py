from django.db import models

from myturkishiid.models import City


class District(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name='İlçe')
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s ' % self.name

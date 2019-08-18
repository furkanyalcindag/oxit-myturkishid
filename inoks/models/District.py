from django.db import models

from inoks.models import City


class District(models.Model):

    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='İl')
    name = models.TextField(blank=True, null=True, verbose_name='İlçe')

    def __str__(self):
        return '%s ' % self.name

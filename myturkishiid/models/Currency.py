from django.db import models


class Currency(models.Model):
    icon = models.ImageField(blank=True, null=True, verbose_name='İkon')
    name = models.TextField(blank=True, null=True, verbose_name='Kur Adı')

    def __str__(self):
        return '%s ' % self.name

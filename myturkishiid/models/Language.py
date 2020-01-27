from django.db import models


class Language(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name='Dil')
    flag = models.ImageField(blank=True, null=True, verbose_name='Bayrak')


    def __str__(self):
        return '%s ' % self.name

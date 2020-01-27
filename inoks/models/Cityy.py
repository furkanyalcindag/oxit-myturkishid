from django.db import models


class City(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name='Yaşadığı Şehir')

    def __str__(self):
        return '%s ' % self.name

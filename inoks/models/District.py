from django.db import models


class District(models.Model):


    name = models.TextField(blank=True, null=True, verbose_name='İlçe')

    def __str__(self):
        return '%s ' % self.name

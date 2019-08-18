from django.db import models


class Job(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name='Meslekler')

    def __str__(self):
        return '%s ' % self.name

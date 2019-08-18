from django.db import models


class OrderSituations(models.Model):
    name = models.TextField(max_length=18500, blank=True, null=True, verbose_name='Sipariş Durumları')

    def __str__(self):
        return '%s ' % self.name

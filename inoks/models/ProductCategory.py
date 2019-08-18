from django.db import models


class ProductCategory(models.Model):
    name = models.TextField(max_length=18500, blank=True, null=True, verbose_name='Ürün Kategorisi')

    def __str__(self):
        return '%s ' % self.name


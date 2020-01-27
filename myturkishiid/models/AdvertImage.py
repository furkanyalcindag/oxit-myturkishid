from django.db import models


class AdvertImage(models.Model):
    advertImage = models.ImageField(upload_to='product/', null=True, blank=True, verbose_name='İlan Resmi')

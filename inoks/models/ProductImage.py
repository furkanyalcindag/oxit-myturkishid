from django.db import models


class ProductImage(models.Model):
    productImage = models.ImageField(upload_to='product/', null=True, blank=True, verbose_name='Ürün Resmi')

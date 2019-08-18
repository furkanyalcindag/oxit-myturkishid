from django.db import models

from inoks.models import Product, Order, Profile
from inoks.models.RefundSituations import RefundSituations


class Refund(models.Model):
    Evet = 'Evt'
    Hayır = 'Hayır'

    OPEN_CHOICES = (
        (Evet, 'Evet'),
        (Hayır, 'Hayır'),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Sipariş Numarası')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Ürün Adı')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Üye Adı')
    orderQuantity = models.TextField(blank=True, null=True, verbose_name='İade Miktarı')
    refundSituations = models.ManyToManyField(RefundSituations)
    refundDate = models.DateTimeField(auto_now_add=True, verbose_name='İade Tarihi')
    isOpen = models.CharField(max_length=128, verbose_name='Cinsiyeti', choices=OPEN_CHOICES, default=Hayır)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')

    def __str__(self):
        return '%s ' % self.name

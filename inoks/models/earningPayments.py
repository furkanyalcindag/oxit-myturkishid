from django.db import models

from inoks.models import Profile


class earningPayments(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile', verbose_name='Ödeme Alan')
    payer_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='payer_profile',
                                      verbose_name='Ödeme Yapan')
    payedDate = models.DateTimeField(verbose_name='Ödeme Tarihi')
    paymentTotal = models.DecimalField(verbose_name='ödeme Tutarı', max_digits=10, decimal_places=2)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')

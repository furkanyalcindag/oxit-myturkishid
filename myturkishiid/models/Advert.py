from django.db import models

from inoks.models.Cityy import City
from myturkishiid.models.AdvertImage import AdvertImage
from myturkishiid.models.District import District
from myturkishiid.models.Feature import Feature
from myturkishiid.models.Category import Category
from myturkishiid.models import FeatureType

from myturkishiid.models.Enums import FLOOR_CHOICES, FLOOR, BATHROOM_CHOICES, BATHROOM, ROOM_CHOICES, ROOM1, \
    BALKONY_CHOICES, BALKONY1, HEATING_CHOICES, HEATING, FRONT_CHOICES, FRONT


class Advert(models.Model):
    advertImage = models.ManyToManyField('AdvertImage', blank=True, verbose_name='Ürün Resmi')
    advertNo = models.CharField(max_length=256, blank=True, null=True, verbose_name='İlan Numarası')
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=False, blank=False, verbose_name='İl')
    district = models.TextField(blank=False, null=False, verbose_name='İlçe')

    category = models.ManyToManyField(Category, verbose_name='İlan Kategorisi', blank=True)
    floorNumber = models.CharField(max_length=256, null=True, blank=True, verbose_name='kat numarası',
                                   choices=FLOOR_CHOICES,
                                   default=FLOOR)
    bathroomNumber = models.CharField(max_length=256, null=True, blank=True, verbose_name='Banyo Sayısı',
                                      choices=BATHROOM_CHOICES,
                                      default=BATHROOM)
    address = models.TextField(blank=True, null=True, verbose_name='Adres')
    room = models.CharField(max_length=128, verbose_name='Oda sayısı', choices=ROOM_CHOICES,
                            default=ROOM1)
    balcony = models.CharField(max_length=256, null=True, blank=True, verbose_name='balkon sayısı',
                               choices=BALKONY_CHOICES,
                               default=BALKONY1)
    heating = models.CharField(max_length=256, null=True, blank=True, verbose_name='Isıtma türü',
                               choices=HEATING_CHOICES,
                               default=HEATING)
    front = models.CharField(max_length=256, null=True, blank=True, verbose_name='Cephe', choices=FRONT_CHOICES,
                             default=FRONT
                             )
    isShow = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
    paidDate = models.DateTimeField(null=True, blank=True, verbose_name='Kayıt Tarihi')
    fieldNet = models.FloatField(null=True, blank=True, verbose_name='Alan Net')
    fieldBrut = models.FloatField(null=True, blank=True, verbose_name='Alan Brüt')
    buildingAge = models.CharField(max_length=256, null=True, blank=True, verbose_name='Bina Yaşı')
    features = models.ManyToManyField(Feature, verbose_name='Özellikler')
    viewCount = models.IntegerField()

    """def __str__(self):complex
        return '%d ' % self.id

    def latest_catch(self):
        if len(self.order_situations.all()) > 0:
            return self.order_situations.all()[len(self.order_situations.all()) - 1]
        else:
            return 0"""

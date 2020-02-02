import django_filters

from myturkishiid.models import Advert
from myturkishiid.models.City import City
from myturkishiid.models.Enums import ROOM_CHOICES


class AdvertFilter(django_filters.FilterSet):
    #price = django_filters.NumericRangeFilter()

    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    room = django_filters.ChoiceFilter(choices=ROOM_CHOICES)
    city = django_filters.ModelChoiceFilter(queryset=City.objects.all())

    class Meta:
        model = Advert
        fields =['room','city',]

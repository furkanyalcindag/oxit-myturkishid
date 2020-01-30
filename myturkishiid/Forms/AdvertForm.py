from django import forms
from django.forms import ModelForm

from myturkishiid.models import Feature
from myturkishiid.models.Category import Category

from myturkishiid.models.Advert import Advert

CHOICES_WITH_BLANK = (
    ('', '--------'),

)


class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = (
            'address',
            'room',
            'price',
            'buildingAge',

            'bathroomNumber',
            'floorNumber',
            'category',
            'fieldBrut',
            'fieldNet',
            'heating',
            'balcony',
            'front',
            'advertNo',
            'city',
            'district'

        )
        widgets = {
            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', 'required': 'required', "onChange": 'ilceGetir()'}),

            'district': forms.Select(
                attrs={'class': 'form-control select2 select2-hidden-accessible',
                       'style': 'width: 100%; ', 'id': 'ilce_id'}
            ),

            'address': forms.Textarea(
                attrs={'class': 'form-control ', 'placeholder': 'Adres', 'rows': '2', 'required': 'required',
                       'style': 'width: 50%;',
                       }),
            'price': forms.NumberInput(
                attrs={'class': 'form-control ', 'placeholder': 'Fiyat (₺)', 'required': 'required'}),
            'advertNo': forms.NumberInput(
                attrs={'class': 'form-control ', 'placeholder': 'İlan Numarası', 'required': 'required'}),
            'room': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%;'}),
            'balcony': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%;'}),
            'front': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                         'style': 'width: 100%;'}),

            'floorNumber': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Kat Numarası', 'required': 'required',
                       }),

            'bathroomNumber': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Banyo Sayısı', 'required': 'required',
                       }),

            'heating': forms.Select(
                attrs={'class': 'form-control select2 select2-hidden-accessible', 'style': 'width:100%',
                       'placeholder': 'Isıtma Tipi',
                       'required': 'required',
                       }),
            'buildingAge': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Bina Yaşı',
                       'required': 'required',
                       }),
            'fieldNet': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Net Alan', 'required': 'required',
                       }),
            'fieldBrut': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Brüt Alan', 'required': 'required',
                       }),
        }

    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    # Overriding __init__ here allows us to provide initial
    # data for 'toppings' field
    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)

        if kwargs.get('instance'):
            print(kwargs.get('instance').category.all())
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            forms.ModelForm.__init__(self, *args, **kwargs)
            initial['category'] = [t.pk for t in kwargs['instance'].category.all()]
            self.fields['category'].initial = initial['category']

        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['category'].widget.attrs = {'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%;', 'data-select2-id': '7',
                                                'data-placeholder': 'Kategori Seçiniz'}

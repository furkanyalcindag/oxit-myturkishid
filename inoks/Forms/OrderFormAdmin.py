from django import forms
from django.forms import ModelForm

from inoks.models import Order, Product, OrderSituations

CHOICES_WITH_BLANK = (
    ('', '--------'),

)


class OrderFormAdmin(ModelForm):
    # product = forms.ModelChoiceField(queryset=Product.objects.all(),
    #                                to_field_name='name',
    #        in                       empty_label="Seçiniz",
    #                              widget=forms.Select(
    #                                 attrs={'class': 'form-control select2 select2-hidden-accessible',
    #                                        'style': 'width: 100%; '}))

    droptxt = forms.CharField(widget=forms.HiddenInput())
    isContract = forms.BooleanField(required=True)

    class Meta:
        model = Order
        fields = (
            'profile', 'city', 'district', 'address',
            'payment_type',
            'isContract')
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%;', "onChange": 'bilgiGetir()'}),

            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible disabled-select',
                                        'style': 'width: 100%; ', "onChange": 'ilceGetir()'}),

             'district': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'ilçe', 'required': 'required' ,'readonly': 'readonly'}),

            'address': forms.Textarea(
                attrs={'class': 'form-control ', 'placeholder': 'Adres', 'rows': '2', 'required': 'required',
                       'readonly': 'readonly'}),

            'payment_type': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%;'})

        }

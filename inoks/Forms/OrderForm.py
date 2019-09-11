from django import forms
from django.forms import ModelForm

from inoks.models import Order, Product, OrderSituations


class OrderForm(ModelForm):
    #product = forms.ModelChoiceField(queryset=Product.objects.all(),
     #                                to_field_name='name',
      #                               empty_label="Seçiniz",
       #                              widget=forms.Select(
        #                                 attrs={'class': 'form-control select2 select2-hidden-accessible',
        #                                        'style': 'width: 100%; '}))

    droptxt = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = (
            'profile',  'city', 'district', 'address',
            'payment_type',
            'isContract')
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%; '}),



            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; '}),

            'district': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                            'style': 'width: 100%; '}),

            'address': forms.Textarea(
                attrs={'class': 'form-control ', 'placeholder': 'Adres', 'rows': '2', 'required': 'required'}),

            'payment_type': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%;'})

        }

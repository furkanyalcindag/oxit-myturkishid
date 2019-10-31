from django import forms
from django.forms import ModelForm

from inoks.models import Order, Product, OrderSituations


CHOICES_WITH_BLANK = (
    ('', '--------'),

)

class OrderForm(ModelForm):
    #product = forms.ModelChoiceField(queryset=Product.objects.all(),
     #                                to_field_name='name',
      #                               empty_label="Seçiniz",
       #                              widget=forms.Select(
        #                                 attrs={'class': 'form-control select2 select2-hidden-accessible',
        #                                        'style': 'width: 100%; '}))

    droptxt = forms.CharField(widget=forms.HiddenInput())
    isContract = forms.BooleanField(required=True)
    class Meta:
        model = Order
        fields = (
            'city', 'district', 'address',
            'payment_type',
            'isContract')
        widgets = {


            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', "onChange":'ilceGetir()'}),

            'district': forms.Select(choices=CHOICES_WITH_BLANK,attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', 'id':'ilce_id'}
              ),




            'address': forms.Textarea(
                attrs={'class': 'form-control ', 'placeholder': 'Adres', 'rows': '2', 'required': 'required'}),

            'payment_type': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%;'})

        }

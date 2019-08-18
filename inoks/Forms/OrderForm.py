from django import forms
from django.forms import ModelForm

from inoks.models import Order, Product


class OrderForm(ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(),
                                     to_field_name='name',
                                     empty_label="Seçiniz",
                                     widget=forms.Select(
                                         attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%; '}))



    class Meta:
        model = Order
        fields = (
            'profile', 'product', 'quantity', 'city', 'district', 'address', 'sponsor',
            'payment_type',
            'isContract')
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%; '}),

            'quantity': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Miktar', 'required': 'required'}),

            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; '}),

            'district': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                            'style': 'width: 100%; '}),

            'address': forms.Textarea(
                attrs={'class': 'form-control ', 'placeholder': 'Adres', 'rows': '2', 'required': 'required'}),

            'sponsor': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Sponsor', 'required': 'required'}),

            'payment_type': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%;'})

        }

from django import forms
from django.forms import ModelForm

from inoks.models import OrderSituations


class OrderSituationsForm(ModelForm):

    class Meta:
        model = OrderSituations
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Sipariş Durumları', 'required': 'required'})


        }
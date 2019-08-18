from django import forms
from django.forms import ModelForm

from inoks.models import RefundSituations


class RefundSituationsForm(ModelForm):

    class Meta:
        model = RefundSituations
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'İade Durumları', 'required': 'required'})


        }
from django import forms
from django.forms import ModelForm

from myturkishiid.models import FeatureDesc


class FeatureDescForm(ModelForm):
    class Meta:
        model = FeatureDesc
        fields = ('lang', 'name')

        widgets = {

            'lang': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Dil', 'required': 'required', 'readonly': 'readonly'}),

            'name': forms.TextInput(
                attrs={'class': 'form-control ', 'rows': '2', 'required': 'required',
                       'placeholder': 'Özellik çeviri'
                       }),

        }

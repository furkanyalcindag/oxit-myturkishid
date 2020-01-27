from django import forms
from django.forms import ModelForm

from myturkishiid.models import Feature


class FeatureForm(ModelForm):
    class Meta:
        model = Feature
        fields = '__all__'
        widgets = {

            'key': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Özellik Adı', 'rows': '2', 'required': 'required'}),
            'featureType': forms.Select(
                attrs={'class': 'form-control ', 'placeholder': 'Başlık', 'rows': '2', 'required': 'required'})
        }

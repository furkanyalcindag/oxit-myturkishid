from django import forms
from django.forms import ModelForm

from myturkishiid.models import FeatureType


class FeatureTypeForm(ModelForm):
    class Meta:
        model = FeatureType
        fields = ('key',)
        widgets = {
            'key': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Özellik Tipi Adı', 'required': 'required'})
        }

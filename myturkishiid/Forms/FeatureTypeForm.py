from django import forms
from django.forms import ModelForm

from myturkishiid.models import FeatureType


class FeatureTypeForm(ModelForm):
    class Meta:
        model = FeatureType
        fields = ('key',)
        widgets = {
            'key': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Özellik Adı', 'rows': '2', 'required': 'required'})
        }

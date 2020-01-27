from django import forms
from django.forms import ModelForm

from myturkishiid.models import CategoryDesc


class CategoryDescForm(ModelForm):
    class Meta:
        model = CategoryDesc
        fields = ('lang', 'name')
        widgets = {

            'lang': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Dil', 'required': 'required', 'readonly': 'readonly'}),

            'name': forms.Textarea(
                attrs={'class': 'form-control ', 'rows': '2', 'required': 'required',
                       }),
        }

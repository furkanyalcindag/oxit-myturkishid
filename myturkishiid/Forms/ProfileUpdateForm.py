from django import forms
from django.forms import ModelForm

from myturkishiid.models.Profile import Profile

CHOICES_WITH_BLANK = (
    ('', '--------'),

)


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile

        fields = (
            'profileImage', 'mobilePhone',)
        widgets = {

            'mobilePhone': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Telefon Numarası', 'required': 'required'}),



        }

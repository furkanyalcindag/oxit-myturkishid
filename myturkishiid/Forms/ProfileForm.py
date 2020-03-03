from django import forms
from django.forms import ModelForm

from myturkishiid.models.Profile import Profile


class ProfileForm(ModelForm):

    class Meta:
        model = Profile

        fields = (
             'mobilePhone', )
        widgets = {

            'mobilePhone': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Telefon Numarası', 'required': 'required',
                       'maxlength': '10', 'minlength': '10'}),


        }

from django import forms
from django.forms import ModelForm

from inoks.models import Profile

CHOICES_WITH_BLANK = (
    ('', '--------'),

)


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile

        fields = (
            'profileImage', 'address', 'mobilePhone', 'gender', 'tc', 'birthDate', 'job', 'city', 'educationLevel',
            'sponsor', 'district','iban')
        widgets = {
            'address': forms.Textarea(
                attrs={'class': 'form-control ', 'placeholder': 'Adres', 'rows': '2', 'required': 'required'}),
            'mobilePhone': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Telefon Numarası', 'required': 'required'}),
            'gender': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%;', 'required': 'required'}),
            'tc': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'T.C. Kimlik Numarası', 'required': 'required','disabled':'disabled'}),

            'birthDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker', 'autocomplete': 'off',
                       'onkeydown': 'return false','disabled':'disabled'}),


            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; ', 'required': 'required', "onChange": 'ilceGetir()'}),

            'district': forms.Select(choices=CHOICES_WITH_BLANK,
                                     attrs={'class': 'form-control select2 select2-hidden-accessible',
                                            'style': 'width: 100%; ', 'id': 'ilce_id'}),

            'job': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                       'style': 'width: 100%;', 'required': 'required'}),

            'educationLevel': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%;', 'required': 'required'}),
            'iban': forms.TextInput(
                attrs={'class': 'form-control iban', 'placeholder': 'iban',
                       'required': 'required',
                       'maxlength': '11', 'minlength': '11'}),
            'sponsor': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%; ', 'required': 'required', 'disabled':'disabled'}),
        }

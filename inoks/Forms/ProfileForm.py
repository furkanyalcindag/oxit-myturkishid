from django import forms
from django.forms import ModelForm

from inoks.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile

        fields = (
            'profileImage', 'address', 'mobilePhone', 'gender', 'tc', 'birthDate', 'job', 'city', 'educationLevel',
            'sponsor', 'district')
        widgets = {
            'address': forms.Textarea(
                attrs={'class': 'form-control ', 'placeholder': 'Adres', 'rows': '2', 'required': 'required'}),
            'mobilePhone': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Telefon Numarası'}),
            'gender': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%;'}),
            'tc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'T.C. Kimlik Numarası'}),

            # 'birthDate': forms.DateInput(
            #     attrs={'class': 'form-control ', 'data-input-mask': '"alias: yyyy-mm-dd', 'data-mask': '"'}),

            'birthDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),

            'sponsor': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%; '}),

            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%; '}),

            'district': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                            'style': 'width: 100%; '}),

            'job': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                       'style': 'width: 100%;'}),

            'educationLevel': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%;'}),
        }

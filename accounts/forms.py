from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'type' :'text', 'id' : 'username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'type': 'password', 'id': 'password'}))



class ResetPassword(PasswordChangeForm):
    old_password = forms.CharField(label="Mevcut Şifre", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(label="Yeni Şifre", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(label="Yeni Şifre Tekrar", max_length=30,
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))


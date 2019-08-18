from django.contrib.auth.models import User
from django.forms import ModelForm, forms


class UserForm(ModelForm):
    # confirm_password = forms.CharField( widget=forms.PasswordInput(
    #   attrs={'class': 'form-control', 'placeholder': 'Şifre Tekrarı'}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'is_active')
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Adınız', 'value': '', 'required': 'required'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': ' Soyadınız', 'required': 'required'}),
            'username': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Kullanıcı Adı', 'required': 'required'}),
            'email': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'E-mailiniz', 'required': 'required'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'iCheck-helper'}),
            # 'password': forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Şifre',}),

        }

        User._meta.get_field_by_name('email').unique = True

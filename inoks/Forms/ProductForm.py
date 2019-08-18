from django import forms
from django.forms import ModelForm

from inoks.models import Product, ProductCategory


class ProductForm(ModelForm):
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(),
                                      to_field_name='name',
                                      empty_label="Seçiniz",
                                      widget=forms.Select(
                                          attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                 'style': 'width: 100%; '}))

    class Meta:
        model = Product
        fields = (
            'productImage', 'name', 'price', 'discountPrice', 'stock', 'category', 'discountStartDate',
            'discountFinishDate', 'info')
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Ürün Adı', 'required': 'required'}),
            'price': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Ürün Fiyatı', 'required': 'required'}),
            'discountPrice': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'İndirimli Fiyatı'}),
            'stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'T.C. Kimlik Numarası'}),

            'discountStartDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),
            'discountFinishDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker2', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),

            'info': forms.Textarea(
                attrs={'class': 'form-control ', 'placeholder': 'Adres', 'rows': '2', 'required': 'required'})
        }

from django import forms
from django.forms import ModelForm

from myturkishiid.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('parent', 'key')
        parent = forms.ModelChoiceField(queryset=Category.objects.all(),
                                        to_field_name='name',
                                        empty_label="Seçiniz",
                                        required=False,
                                        widget=forms.Select(
                                            attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                   'style': 'width: 100%; '}))

    widgets = {

        'key': forms.TextInput(
            attrs={'class': 'form-control ', 'rows': '2', 'required': 'required',
                   }),

    }

from django import forms
from django.forms import ModelForm

from inoks.models import Product, ProductCategory


class ProductForm(ModelForm):
    # category = forms.ChoiceField(choices=[(doc.id, doc.name) for doc in ProductCategory.objects.all()],
    #                            widget=forms.Select(
    #                               attrs={'class': 'form-control select2 select2-hidden-accessible',
    #                                     'style': 'width: 100%; '})

    class Meta:
        model = Product
        fields = (
            'productImage', 'name', 'price', 'stock', 'category',  'info')
        labels = {
            'price': 'Ürün Fiyatı',



        }
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control ', 'placeholder': 'Ürün Adı', 'required': 'required'}),
            'price': forms.NumberInput(
                attrs={'class': 'form-control ', 'placeholder': 'Ürün Fiyatı', 'required': 'required'}),
            'discountPrice': forms.NumberInput(attrs={'class': 'form-control ', 'placeholder': 'İndirimli Fiyatı'}),
            'stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Stok', 'required': 'required'}),

            'discountStartDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker', 'autocomplete': 'off',
                       'onkeydown': 'return false','required':'false'}),
            'discountFinishDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker2', 'autocomplete': 'off',
                       'onkeydown': 'return false'}),

            'info': forms.Textarea(
                attrs={'class': 'form-control ', 'placeholder': 'Ürün Bilgileri', 'rows': '4', 'required': 'required'}),

        }

    category = forms.ModelMultipleChoiceField(queryset=ProductCategory.objects.all())

    # Overriding __init__ here allows us to provide initial
    # data for 'toppings' field
    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)

        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['category'] = [t.pk for t in kwargs['instance'].category.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['category'].widget.attrs = {'class': 'form-control select2 select2-hidden-accessible',
                                                'style': 'width: 100%;', 'data-select2-id': '7',
                                                'data-placeholder': 'Kategori Seçiniz'}

    # def __init__(self, *args, **kwargs):
    #   super(ProductForm, self).__init__(*args, **kwargs)

    #  self.fields['category'].empty_label = 'Seçiniz'

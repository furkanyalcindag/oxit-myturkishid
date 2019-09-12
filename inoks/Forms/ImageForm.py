from django.forms import ModelForm

from inoks.models.ProductImage import ProductImage


class ImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ('productImage',)

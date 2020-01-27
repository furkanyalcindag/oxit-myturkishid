from django.forms import ModelForm

from myturkishiid.models.AdvertImage import AdvertImage


class ImageForm(ModelForm):
    class Meta:
        model = AdvertImage
        fields = ('advertImage',)

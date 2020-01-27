from django import forms
from django.forms import ModelForm

from myturkishiid.models import Feature


class FeatureSaveForm(ModelForm):
    class Meta:
        model = Feature
        fields = '__all__'

    feature = forms.ModelMultipleChoiceField(queryset=Feature.objects.all())

    # Overriding __init__ here allows us to provide initial
    # data for 'toppings' field
    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)

        forms.ModelForm.__init__(self, *args, **kwargs)

        self.fields['feature'].widget.attrs = {'class': 'form-control select2 select2-hidden-accessible',
                                               'style': 'width: 100%;', 'data-select2-id': '7',
                                               'data-placeholder': 'Özellik Seçiniz'}

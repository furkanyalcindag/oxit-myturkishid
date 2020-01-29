from django.contrib import messages
from django.shortcuts import redirect, render

from myturkishiid.Forms.AdvertDescForm import AdvertDescForm
from myturkishiid.Forms.AdvertForm import AdvertForm
from myturkishiid.Forms.CategoryForm import CategoryForm
from myturkishiid.models import Advert, AdvertDesc
from myturkishiid.models.AdvertImage import AdvertImage
from myturkishiid.models.Language import Language


def advert_save(request):
    form_advert = AdvertForm(request.POST or None)

    if request.method == 'POST':

        if form_advert.is_valid():
            advert = Advert(

                room=form_advert.cleaned_data['room'],
                address=form_advert.cleaned_data['address'],
                city=form_advert.cleaned_data['city'],
                district=form_advert.cleaned_data['district'],
                price=form_advert.cleaned_data['price'],
                floorNumber=form_advert.cleaned_data['floorNumber'],
                buildingAge=form_advert.cleaned_data['buildingAge'],
                balcony=form_advert.cleaned_data['balcony'],
                fieldBrut=form_advert.cleaned_data['fieldBrut'],
                fieldNet=form_advert.cleaned_data['fieldNet'],
                bathroomNumber=form_advert.cleaned_data['bathroomNumber']

            )
            advert.save()
            for f in request.FILES.getlist('input2[]'):
                advertImages = AdvertImage(advertImage=f)
                advertImages.save()
                advert.advertImage.add(advertImages)

            advert.save()
            for category in form_advert.cleaned_data['category']:
                advert.category.add(category)
            advert.save()

            """for feature in form_advert.cleaned_data['feature']:
                advert.feature.add(feature)
            advert.save()"""

            messages.success(request, 'ilan Kaydedildi.')

            return redirect('myturkishid:advert-save')


        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'adverttemp/advert-save.html', {'form_advert': form_advert})


def AdvertDesc_save(request, pk):
    form_advertDesc = AdvertDescForm(request.POST)
    advert = Advert.objects.get(pk=pk)
    advertDesc = AdvertDesc.objects.filter(advert=advert)
    lang = Language.objects.all()

    if request.method == 'POST':

        if form_advertDesc.is_valid():
            form = form_advertDesc.save(commit=False)
            form.advert = advert
            form.save()
            messages.success(request, 'Kategori Kaydedildi.')

            return redirect('myturkishid:advertDesc-save', pk)

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'adverttemp/advertDesc-save.html',
                  {'form_advertDesc': form_advertDesc, 'advert': advert, 'lang': lang, 'advertDesc': advertDesc})


def get_adverts(request):
    adverts = Advert.objects.all()

    return render(request, 'adverttemp/get-advert.html', {'adverts': adverts})

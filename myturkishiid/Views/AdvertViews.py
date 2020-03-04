from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms import modelformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render

from myturkishiid.Forms import ImageForm
from myturkishiid.Forms.AdvertDescForm import AdvertDescForm
from myturkishiid.Forms.AdvertForm import AdvertForm
from myturkishiid.Forms.CategoryForm import CategoryForm
from myturkishiid.models import Advert, AdvertDesc, FeatureType, Feature, AdvertObject
from myturkishiid.models.AdvertImage import AdvertImage
from myturkishiid.models.Language import Language
from myturkishiid.services import general_methods


@login_required
def advert_save(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
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


@login_required
def AdvertDesc_save(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    form_advertDesc = AdvertDescForm(request.POST)
    advert = Advert.objects.get(pk=pk)
    advertDesc = AdvertDesc.objects.filter(advert=advert)
    lang = Language.objects.all()

    if request.method == 'POST':

        if form_advertDesc.is_valid():
            form = form_advertDesc.save(commit=False)
            form.advert = advert
            form.save()
            messages.success(request, 'Başarıyla Kaydedildi.')

            return redirect('myturkishid:advertDesc-save', pk)

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'adverttemp/advertDesc-save.html',
                  {'form_advertDesc': form_advertDesc, 'advert': advert, 'lang': lang, 'advertDesc': advertDesc})


@login_required
def delete_advertDesc(request, advert_id, advertDesc_id):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    # advert = Advert.objects.get(pk=advert_id)
    advertDesc = AdvertDesc.objects.get(pk=advertDesc_id)
    advertDesc.delete()
    advertDesc.advert.save()
    messages.success(request, 'Çeviri Başarıyla Silindi')
    return redirect('myturkishid:advertDesc-save', advert_id)


@login_required
def advertDesc_update(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    advertdesc = AdvertDesc.objects.get(pk=pk)
    advertDesc_form = AdvertDescForm(request.POST or None, instance=advertdesc)

    if request.method == 'POST':
        if advertDesc_form.is_valid():

            advertDesc_form.save()

            messages.success(request, 'Başarıyla Güncellendi')

            return redirect('myturkishid:advertDesc-save', advertdesc.advert.pk)

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'adverttemp/advertDesc-update.html',
                  {'advertDesc': advertDesc_form})


@login_required
def get_adverts(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    adverts = Advert.objects.all().order_by('-id')
    objects = []
    lang = Language.objects.get(code='tr')

    for advert in adverts:
        if advert.advertdesc_set.filter(lang=lang).count() == 0:
            advertDesc = None
        else:
            advertDesc = advert.advertdesc_set.filter(lang=lang)[0]
        advertObject = AdvertObject(advert=advert, desc=advertDesc, category=None)
        objects.append(advertObject)
    return render(request, 'adverttemp/get-advert.html', {'adverts': objects})


@login_required
def add_feature_to_advert(request, advert_id):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    advert = Advert.objects.get(pk=advert_id)

    exist_features = Feature.objects.filter(id__in=advert.features.all().values('pk'))

    features = Feature.objects.filter(~Q(id__in=advert.features.all().values('pk')))

    if request.method == 'POST':
        for check in request.POST.getlist('check_list[]'):
            feature = Feature.objects.get(pk=int(check))
            advert.features.add(feature)
            advert.save()

        messages.success(request, 'özellikler eklendi.')

        return redirect('myturkishid:add-features-to-advert', advert_id)

    return render(request, 'adverttemp/add-feature-to-advert.html',
                  {'advert': advert, 'exist_features': exist_features, 'features': features})


@login_required
def delete_feature_from_advert(request, feature_id, advert_id):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    feature = Feature.objects.get(pk=feature_id)
    advert = Advert.objects.get(pk=advert_id)
    advert.features.remove(feature)
    advert.save()
    messages.success(request, 'Özellik ilandan başarıyla çıkarıldı.')
    return redirect('myturkishid:add-features-to-advert', advert.pk)


@login_required
def advert_update(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    advert = Advert.objects.get(id=pk)
    advert_form = AdvertForm(request.POST or None, instance=advert)
    durum = 'GUNCELLE'
    images = advert.advertImage.all()

    if request.method == 'POST':
        if advert_form.is_valid():

            advert.category.clear()
            for category in advert_form.cleaned_data['category']:
                advert.category.add(category)

            advert.save()

            for f in request.FILES.getlist('input2[]'):
                advertImages = AdvertImage(advertImage=f)
                advertImages.save()
                advert.advertImage.add(advertImages)

            advert.save()

            messages.success(request, 'Başarıyla Güncellendi')

            return redirect('myturkishid:get-advert')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'adverttemp/advert-update.html',
                  {'form_advert': advert_form, 'images': images, 'advert': advert.pk, 'durum': durum,
                   'ilce': advert.district})


@login_required
def advert_image_delete(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.POST:
        try:
            image_id = request.POST.get('image_id')
            advert_id = request.POST.get('advert_id')

            advert = Advert.objects.get(pk=advert_id)
            image = AdvertImage.objects.get(pk=image_id)

            advert.advertImage.remove(image)
            advert.save()
            image.delete()

            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})

        except Exception as e:

            return JsonResponse({'status': 'Fail', 'msg': e})


@login_required
def advert_delete(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    if request.POST:
        try:

            advert_id = request.POST.get('advert_id')
            advert = Advert.objects.get(pk=advert_id)
            advert.delete()

            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})

        except Exception as e:

            return JsonResponse({'status': 'Fail', 'msg': e})

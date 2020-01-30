from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect

from myturkishiid.Forms.CategoryDesc import CategoryDescForm
from myturkishiid.Forms.CategoryForm import CategoryForm
from myturkishiid.Forms.FeatureDescForm import FeatureDescForm
from myturkishiid.Forms.FeatureForm import FeatureForm
from myturkishiid.Forms.FeatureSaveForm import FeatureSaveForm
from myturkishiid.Forms.FeatureTypeDescForm import FeatureTypeDescForm
from myturkishiid.Forms.FeatureTypeForm import FeatureTypeForm
from myturkishiid.models import FeatureType, Feature, FeatureDesc, FeatureTypeDesc, Category, CategoryDesc, Advert

from myturkishiid.models.Language import Language


def feature_save(request):
    form_feature = FeatureForm(request.POST)
    features = Feature.objects.all()

    if request.method == 'POST':

        if form_feature.is_valid():
            form_feature.save()
            messages.success(request, 'özellik Kaydedildi.')

            return redirect('myturkishid:feature-save')


        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'featuretemp/feature-save.html', {'form_feature': form_feature, 'features': features})


def featureType_save(request):
    form_featureType = FeatureTypeForm(request.POST)

    if request.method == 'POST':

        if form_featureType.is_valid():
            form_featureType.save()

            messages.success(request, 'Başlık Kaydedildi.')

            return redirect('myturkishid:featureType-save')


        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'featuretemp/featureType-save.html', {'form_featureType': form_featureType})


def get_feature(request):
    feature = Feature.objects.all()

    return render(request, 'featuretemp/get-feature.html', {'feature': feature})


def featureDesc_save(request, pk):
    form_featureDesc = FeatureDescForm(request.POST)
    feature = Feature.objects.get(pk=pk)
    featureDesc = FeatureDesc.objects.filter(feature=feature)
    lang = Language.objects.all()

    if request.method == 'POST':

        if form_featureDesc.is_valid():
            form = form_featureDesc.save(commit=False)
            form.feature = feature
            form.save()
            messages.success(request, 'Kaydedildi.')

            return redirect('myturkishid:featureDesc-save', pk)

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'featuretemp/FeatureDesc-save.html',
                  {'form_featureDesc': form_featureDesc, 'featureDesc': featureDesc, 'lang': lang, 'feature': feature,
                   })


def feature_type(request):
    feature_types = FeatureType.objects.all()

    form_featureType = FeatureTypeForm(request.POST)

    if request.method == 'POST':

        if form_featureType.is_valid():
            form_featureType.save()

            messages.success(request, 'Başlık Kaydedildi.')

            return redirect('myturkishid:feature-type')


        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'featuretemp/feature-types.html',
                  {'types': feature_types, 'form_featureType': form_featureType})


def featureTypeDesc_save(request, pk):
    form_featureTypeDesc = FeatureTypeDescForm(request.POST)
    featureType = FeatureType.objects.get(pk=pk)
    featureTypeDesc = FeatureTypeDesc.objects.filter(featureType=featureType)

    lang = Language.objects.all()

    if request.method == 'POST':

        if form_featureTypeDesc.is_valid():
            form = form_featureTypeDesc.save(commit=False)
            form.featureType = featureType
            form.save()
            messages.success(request, 'Kaydedildi.')

            return redirect('myturkishid:featureTypeDesc-save', pk)

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'featuretemp/featureTypeDesc-save.html',
                  {'form': form_featureTypeDesc, 'featureType': featureType, 'lang': lang, 'descs': featureTypeDesc})


def featureType_feature_save(request, pk, ):
    featureForm = FeatureSaveForm(request.POST)
    featureType = FeatureType.objects.filter(pk=pk)
    advert = Advert.objects.get(featureType=featureType)

    if request.method == 'POST':
        featureForm.save()
        if featureForm.is_valid():
            featureForm = featureForm.save(commit=False)
            for feature in featureForm.cleaned_data['feature']:
                advert.feature.add(feature)
            featureForm.save()

            messages.success(request, 'özellik Kaydedildi.')

            return redirect('myturkishid:feature-save')


        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'featuretemp/add-type-to-feature.html', {'featureForm': featureForm, })


def get_featureType_advert(request, pk):
    advert = Advert.objects.get(pk=pk)
    featureTypes = FeatureType.objects.all()

    return render(request, 'featuretemp/add-type-to-feature.html', {'advert': advert, 'featureTypes': featureTypes})


def add_feature_to_advert(request, advert_id, featuretype_id):
    advert = Advert.objects.get(pk=advert_id)
    exist_features = advert.feature.filter(featuretype_id=featuretype_id)
    features = Feature.objects.filter(featureType_id=featuretype_id)
    return render(request, '', {'features': features})


def add_feature_to_feature_type(request, featuretype_id):
    exist_features = Feature.objects.filter(featureType_id=featuretype_id)
    features = Feature.objects.filter(~Q(featureType_id=featuretype_id))
    feature_type = FeatureType.objects.get(id=featuretype_id)

    if request.method == 'POST':
        for check in request.POST.getlist('check_list[]'):
            feature = Feature.objects.get(pk=int(check))
            feature.featureType = feature_type
            feature.save()

        messages.success(request, 'özellikler eklendi.')

        return redirect('myturkishid:add-features-to-feature-type', featuretype_id)

    return render(request, 'featuretemp/add-feature-to-feature-type.html',
                  {'features': features, 'exist_features': exist_features,'type':feature_type})


def delete_feature_from_feature_type(request,feature_id):
    feature=Feature.objects.get(pk=feature_id)
    x = feature.featureType
    feature.featureType=None
    feature.save()
    messages.success(request, 'özellikler çıkarıldı.')
    return redirect('myturkishid:add-features-to-feature-type', x.pk)

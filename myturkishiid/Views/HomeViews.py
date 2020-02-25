from django.http import HttpResponse
from django.shortcuts import render, redirect

from myturkishiid.filters.AdvertFilter import AdvertFilter
from myturkishiid.models import Advert, FeatureType
from myturkishiid.models.AdvertObject import AdvertObject
from myturkishiid.models.AdvertObjectHome import AdvertObjectHome
from myturkishiid.models.Language import Language


def index(request):
    adverts = Advert.objects.all()
    advertsObjects = []
    lang = None

    filter = AdvertFilter(request.GET, queryset=adverts)

    if not ('lang' in request.COOKIES):
        lang = Language.objects.get(code='fa')
    else:
        lang = Language.objects.get(id=request.COOKIES['lang'])
    if not filter.qs is None:
        advertDesc = None
        for advert in filter.qs:
            category = advert.category.all()[0]
            if advert.advertdesc_set.filter(lang=lang) and category.categorydesc_set.filter(lang=lang):
                advertDesc = advert.advertdesc_set.filter(lang=lang)[0]
                category = category.categorydesc_set.filter(lang=lang)[0]
                advertObject = AdvertObject(advert=advert, desc=advertDesc, category=category)
                advertsObjects.append(advertObject)

    else:
        for advert in adverts:
            category = advert.category.all()[0]
            if advert.advertdesc_set.filter(lang=lang) and category.categorydesc_set.filter(lang=lang):
                advertDesc = advert.advertdesc_set.filter(lang=lang)[0]
                category = category.categorydesc_set.filter(lang=lang)[0]
                advertObject = AdvertObject(advert=advert, desc=advertDesc, category=category)
                advertsObjects.append(advertObject)

    return render(request, 'hometemp/home-page.html', {'adverts': advertsObjects, 'lang': lang, 'filter': filter})


def setcookie(request, pk):
    response = redirect('myturkishid:home')
    response.set_cookie(key='lang', value=pk, expires=60 * 60 * 60 * 60 * 60)

    return response


def get_advert(request, pk):
    if not ('lang' in request.COOKIES):
        lang = Language.objects.get(code='fa')
    else:
        lang = Language.objects.get(id=request.COOKIES['lang'])

    advert = Advert.objects.get(pk=pk)
    advert.viewCount = advert.viewCount + 1
    advert.save()
    category = advert.category.all()[0]
    category = category.categorydesc_set.filter(lang=lang)[0]

    advertDesc = advert.advertdesc_set.filter(lang=lang)[0]

    last_dict = dict()

    for type in FeatureType.objects.all():

        feature_dict = dict()
        feature_dict.clear()
        for feature in advert.features.all():

            if feature.featureType == type:
                feature_dict[feature.key] = feature.featuredesc_set.filter(lang=lang)[0]

        if len(feature_dict) > 0:
            last_dict[type.featuretypedesc_set.filter(lang=lang)[0].name] = feature_dict

    advertObject = AdvertObjectHome(advert=advert, desc=advertDesc, category=category, features=last_dict)

    return render(request, 'hometemp/advert-detail_home.html', {'advert': advertObject, 'lang': lang})

from django.http import HttpResponse
from django.shortcuts import render, redirect

from myturkishiid.filters.AdvertFilter import AdvertFilter
from myturkishiid.models import Advert
from myturkishiid.models.AdvertObject import AdvertObject
from myturkishiid.models.Language import Language


def index(request):
    adverts = Advert.objects.all()
    advertsObjects = []
    lang = None

    filter = AdvertFilter(request.GET, queryset=adverts)

    if not ('lang' in request.COOKIES):
        lang = Language.objects.get(code='tr')
    else:
        lang = Language.objects.get(id=request.COOKIES['lang'])

    for advert in filter.qs:
        advertDesc = advert.advertdesc_set.filter(lang=lang)[0]
        category = advert.category.all()[0]
        category = category.categorydesc_set.filter(lang=lang)[0]
        advertObject = AdvertObject(advert=advert, desc=advertDesc, category=category)
        advertsObjects.append(advertObject)

    return render(request, 'hometemp/home-page.html', {'adverts': advertsObjects, 'lang': lang, 'filter': filter})


def setcookie(request, pk):
    response = redirect('myturkishid:home')
    response.set_cookie(key='lang', value=pk, expires=7)

    return response

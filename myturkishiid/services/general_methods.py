from myturkishiid.models import Menu
from myturkishiid.models.Language import Language


def getMenu(request):
    menus = Menu.objects.all().order_by('name')

    return {'menus': menus}


def languages(request):
    languages = Language.objects.all()

    lang=None

    if not ('lang' in request.COOKIES):
        lang = Language.objects.get(code='tr')
    else:
        lang = Language.objects.get(id=request.COOKIES['lang'])



    return {'langs':languages, 'lang':lang}
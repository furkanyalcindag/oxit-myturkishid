from myturkishiid.models import Menu


def getMenu(request):
    menus = Menu.objects.all().order_by('name')

    return {'menus': menus}
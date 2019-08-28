from inoks.models import Profile, Order, Menu, MenuAdmin


def getMenu(request):
    menus = Menu.objects.all()
    return {'menus': menus}


def getAdminMenu(request):
    adminmenus = MenuAdmin.objects.all()
    return {'adminmenus': adminmenus}


def activeUser(request, pk):
    user = Profile.objects.get(pk=pk)
    user.isApprove = True
    user.user.is_active = True
    user.save()
    user.user.save()
    return user


def passiveUser(request, pk):
    user = Profile.objects.get(pk=pk)
    user.user.is_active = False
    user.save()
    user.user.save()
    return user


def reactiveUser(request, pk):
    user = Profile.objects.get(pk=pk)
    user.user.is_active = True
    user.save()
    user.user.save()
    return user


def activeOrder(request, pk):
    order = Order.objects.get(pk=pk)
    order.isApprove = True
    order.save()
    return order

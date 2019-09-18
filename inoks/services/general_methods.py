import datetime

from django.contrib.auth.models import User

from inoks.models import Profile, Order, Menu, MenuAdmin, Refund
from inoks.models.ProfileControlObject import ProfileControlObject


def getMenu(request):
    menus = Menu.objects.all()
    return {'menus': menus}


def getAdminMenu(request):
    adminmenus = MenuAdmin.objects.all()
    return {'adminmenus': adminmenus}


def activeUser(request, pk):
    user = Profile.objects.get(pk=pk)
    user.isApprove = True
    user.activePassiveDate = datetime.datetime.now()
    user.user.is_active = True
    user.save()
    user.user.save()
    return user


def passiveUser(request, pk):
    user = Profile.objects.get(pk=pk)
    user.user.is_active = False
    user.activePassiveDate = datetime.datetime.now()
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


def activeRefund(request, pk):
    refund = Refund.objects.get(pk=pk)
    refund.isApprove = True
    refund.save()
    return refund


def passiveRefund(request, pk):
    refund = Refund.objects.get(pk=pk)
    refund.isApprove = False
    refund.save()
    return refund


def existMail(mail):
    users = User.objects.filter(email=mail)
    if len(users) == 0:
        return False
    else:
        return True


# sponsor sponsor  olanları getir
def rtrnProfileBySponsorID(profile_list):
    # profiles = Profile.objects.filter(sponsor=sponsor)

    copy_profile_list = profile_list.copy()

    for prof in copy_profile_list:

        if not prof.is_controlled:
            profiles = Profile.objects.filter(sponsor=prof.profile)
            for profile in profiles:
                profile_object = ProfileControlObject(profile=profile, is_controlled=False)
                profile_list.append(profile_object)

            for index in range(len(profile_list)):
                if profile_list[index] == prof:
                    profile_list[index].is_controlled = True

    res = sum(1 for i in profile_list if not i.is_controlled)

    if res == 0:
        return profile_list

    return rtrnProfileBySponsorID(profile_list)

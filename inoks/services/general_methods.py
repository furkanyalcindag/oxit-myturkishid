import calendar
import datetime

from django.contrib.auth.models import User
from django.db.models import Sum

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
                total_order = monthlyMemberOrderTotal(profile)['total_price']
                if total_order is None:
                    total_order = 0
                total_order = str(float(str(total_order).replace(",", ".")))

                profile_object = ProfileControlObject(profile=profile, is_controlled=False,
                                                      total_order=total_order)
                profile_list.append(profile_object)

            for index in range(len(profile_list)):
                if profile_list[index] == prof:
                    profile_list[index].is_controlled = True

    res = sum(1 for i in profile_list if not i.is_controlled)

    if res == 0:
        return profile_list

    return rtrnProfileBySponsorID(profile_list)


def monthlyMemberOrderTotal(profile):
    datetime_current = datetime.datetime.today()
    year = datetime_current.year
    month = datetime_current.month
    num_days = calendar.monthrange(year, month)[1]

    datetime_start = datetime.datetime(year, month, 1, 0, 0)

    datetime_end = datetime.datetime(year, month, num_days, 23, 59)

    # scores = Score.objects.filter(creationDate__range=(datetime_start, datetime_end)).order_by('score')[:100]
    order2 = Order.objects.filter(creationDate__range=(datetime_start, datetime_end)).filter(
        profile=profile)
    orders_sum = Order.objects.filter(creationDate__range=(datetime_start, datetime_end)).filter(
        profile=profile).aggregate(
        total_price=Sum('totalPrice'))

    return orders_sum


def monthlyMemberOrderTotalByDate(profile, month, year):
    datetime_current = datetime.datetime.today()
    year = year
    month = month
    num_days = calendar.monthrange(year, month)[1]

    datetime_start = datetime.datetime(year, month, 1, 0, 0)

    datetime_end = datetime.datetime(year, month, num_days, 23, 59)

    # scores = Score.objects.filter(creationDate__range=(datetime_start, datetime_end)).order_by('score')[:100]
    order2 = Order.objects.filter(creationDate__range=(datetime_start, datetime_end)).filter(
        profile=profile)
    orders_sum = Order.objects.filter(creationDate__range=(datetime_start, datetime_end)).filter(
        profile=profile).aggregate(
        total_price=Sum('totalPrice'))

    return orders_sum


def returnLevelTreeByDate(profileArray, levelDict, level, month, year):
    profiles = []
    profiles = Profile.objects.filter(id__in=profileArray)
    profile_list = []

    for profile in profiles:
        total_order = monthlyMemberOrderTotalByDate(profile, month, year)['total_price']
        if total_order is None:
            total_order = 0
        total_order = str(float(str(total_order).replace(",", ".")))

        profile_object = ProfileControlObject(profile=profile, is_controlled=False,
                                              total_order=total_order)
        profile_list.append(profile_object)

    levelDict[str(level)] = profile_list

    id_array = []

    if level < 7:
        for profile in profiles:

            profileSponsor = Profile.objects.filter(sponsor__id=profile.id)

            for sponsor in profileSponsor:
                id_array.append(sponsor.id)

        returnLevelTreeByDate(id_array, levelDict, level + 1,month,year)

    elif level == 7:
        return levelDict

    else:
        return 0


def returnLevelTree(profileArray, levelDict, level):
    profiles = []
    profiles = Profile.objects.filter(id__in=profileArray)
    profile_list = []

    for profile in profiles:
        total_order = monthlyMemberOrderTotal(profile)['total_price']
        if total_order is None:
            total_order = 0
        total_order = str(float(str(total_order).replace(",", ".")))

        profile_object = ProfileControlObject(profile=profile, is_controlled=False,
                                              total_order=total_order)
        profile_list.append(profile_object)

    levelDict[str(level)] = profile_list

    id_array = []

    if level < 7:
        for profile in profiles:

            profileSponsor = Profile.objects.filter(sponsor__id=profile.id)

            for sponsor in profileSponsor:
                id_array.append(sponsor.id)

        returnLevelTree(id_array, levelDict, level + 1)

    elif level == 7:
        return levelDict

    else:
        return 0


def calculate_earning(levelDict, level):
    earning = 0

    if level == 1:
        return 0

    if level == 2:
        if len(levelDict[str(level)]) == 3:

            for orderPrice in levelDict[str(level)]:
                earning = earning + float(orderPrice.total_order)

            if earning < 2500:
                return 0
            else:
                return float(earning * 6 / 100)

    if level == 3:
        if len(levelDict[str(level)]) == 9:
            for orderPrice in levelDict[str(level)]:
                earning = earning + float(orderPrice.total_order)

            if earning < 7500:
                return 0
            else:
                return float(earning * 5 / 100)

    if level == 4:

        for orderPrice in levelDict[str(level)]:
            earning = earning + float(orderPrice.total_order)

        if earning < 22500:
            return 0
        else:
            return float(earning * 4 / 100)

    if level == 5:

        for orderPrice in levelDict[str(level)]:
            earning = earning + float(orderPrice.total_order)

        if earning < 67500:
            return 0
        else:
            return float(earning * 3 / 100)

    if level == 6:

        for orderPrice in levelDict[str(level)]:
            earning = earning + float(orderPrice.total_order)

        if earning < 202500:
            return 0
        else:
            return float(earning * 2 / 100)

    if level == 7:

        for orderPrice in levelDict[str(level)]:
            earning = earning + float(orderPrice.total_order)

        if earning < 607500:
            return 0
        else:
            return float(earning * 1 / 100)
    return 0

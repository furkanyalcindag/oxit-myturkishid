import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from inoks.models import Order, Profile
from inoks.services import general_methods


@login_required
def return_my_earnings_report(request):
    current_user = request.user
    userprofile = Profile.objects.get(user=current_user)

    total_my_orders = Order.objects.filter(isApprove=True, profile_id=userprofile.id).count()
    orders = Order.objects.filter(isApprove=True, profile_id=userprofile.id)
    return render(request, 'kazanclar/kazanclarim.html', {'orders': orders, 'total_my_orders': total_my_orders})


@login_required
def return_all_earnings_report(request):
    total_my_orders = Order.objects.filter(isApprove=True).count()
    orders = Order.objects.filter(isApprove=True)

    return render(request, 'kazanclar/kazanclar.html', {'orders': orders, 'total_my_orders': total_my_orders})


@login_required
def return_odenenler(request):
    return render(request, 'kazanclar/odenenler.html')


@login_required
def return_odenecekler(request):
    userprofile = Profile.objects.filter(user__is_active=True)
    earnDict = dict()
    total = 0
    total_paid = 0
    not_paid = 0
    datetime_current = datetime.datetime.today()
    year = datetime_current.year
    month = datetime_current.month
    part = str(month) + "/" + str(year)
    for user in userprofile:

        profileArray = []
        levelDict = dict()
        level = 1
        total_earning = 0

        profileArray.append(user.id)

        general_methods.returnLevelTree(profileArray, levelDict, level)

        for i in range(7):
            total_earning = float(total_earning) + float(general_methods.calculate_earning(levelDict, i + 1))

        earnDict[user] = total_earning

    for key in earnDict:
        total = total + int(earnDict[key])

    if request.method == 'POST':
        userprofile = Profile.objects.filter(user__is_active=True)
        earnDict = dict()
        total = 0
        total_paid = 0
        not_paid = 0

        part = request.POST['ay'] + "/" + request.POST['yil']

        for user in userprofile:

            profileArray = []
            levelDict = dict()
            level = 1
            total_earning = 0

            profileArray.append(user.id)

            general_methods.returnLevelTreeByDate(profileArray, levelDict, level, int(request.POST['ay']),
                                                  int(request.POST['yil']))

            for i in range(7):
                total_earning = float(total_earning) + float(general_methods.calculate_earning(levelDict, i + 1))

            earnDict[user] = total_earning

        for key in earnDict:
            total = total + int(earnDict[key])

        return render(request, 'kazanclar/odenecekler.html',
                      {"earnDict": earnDict, 'total': total, 'total_paid': total_paid, 'not_paid': not_paid, 'part':part})

    return render(request, 'kazanclar/odenecekler.html',
                  {"earnDict": earnDict, 'total': total, 'total_paid': total_paid, 'not_paid': not_paid, 'part':part})


def calculate_earning(request):
    userprofile = Profile.objects.filter(user__is_active=True)

    earnDict = dict()

    for user in userprofile:

        profileArray = []
        levelDict = dict()
        level = 1
        total_earning = 0

        profileArray.append(user.id)

        general_methods.returnLevelTree(profileArray, levelDict, level)

        for i in range(7):
            total_earning = float(total_earning) + float(general_methods.calculate_earning(levelDict, i + 1))

        earnDict[user] = total_earning

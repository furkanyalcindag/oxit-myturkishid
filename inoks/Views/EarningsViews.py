import datetime

from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.shortcuts import render

from inoks.models import Order, Profile, earningPayments
from inoks.models.TotalOrderObject import TotalOrderObject
from inoks.services import general_methods


@login_required
def return_my_earnings_report(request):
    userprofile = Profile.objects.filter(user=request.user)
    earnDict = dict()
    earningArray = []
    total = float(0.00)
    total_paid = 0
    not_paid = 0
    datetime_current = datetime.datetime.today()
    year = datetime_current.year
    month = datetime_current.month
    part = str(month) + "/" + str(year)
    total_paid = general_methods.monthlyTotalPaidByDate(str(month), str(year))
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
        total_object = TotalOrderObject(profile=None, total_price=0, earning=0, is_paid=False, paid_date=None)
        total_object.profile = user
        total_object.earning = total_earning
        total_object.total_price = general_methods.monthlyMemberOrderTotal(user, )
        payment = earningPayments.objects.filter(profile=user,
                                                 payedDate=part)
        if payment.count() > 0:
            total_object.is_paid = True
            total_object.paid_date = payment[0].creationDate

        earningArray.append(total_object)

    for key in earnDict:
        total = total + float(earnDict[key])

    if request.method == 'POST':
        userprofile = Profile.objects.filter(user=request.user)
        earnDict = dict()
        earningArray = []
        total = 0
        total_paid = 0
        not_paid = 0

        total_paid = general_methods.monthlyTotalPaidByDate(request.POST['ay'], request.POST['yil'])

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
            total_object = TotalOrderObject(profile=None, total_price=0, earning=0, is_paid=False, paid_date=None)
            total_object.profile = user
            total_object.earning = total_earning
            total_object.total_price = general_methods.monthlyMemberOrderTotalByDate(user, int(request.POST['ay']),
                                                                                     int(request.POST['yil']))
            payment = earningPayments.objects.filter(profile=user,
                                                     payedDate=request.POST['ay'] + "/" + request.POST['yil'])
            if payment.count() > 0:
                total_object.is_paid = True
                total_object.paid_date = payment[0].creationDate

            earningArray.append(total_object)

        for key in earnDict:
            total = total + float(earnDict[key])

        return render(request, 'kazanclar/kazanclarim.html',
                      {"earnDict": earningArray, 'total': total, 'total_paid': total_paid,
                       'not_paid': float(total) - float(total_paid),
                       'part': part, 'month': request.POST['ay'], 'year': request.POST['yil']})
    return render(request, 'kazanclar/kazanclarim.html',
                  {"earnDict": earningArray, 'total': total, 'total_paid': total_paid,
                   'not_paid': float(total) - float(total_paid),
                   'part': part, 'month': str(month), 'year': str(year)})


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
    earningArray = []
    total = float(0.00)
    total_paid = 0
    not_paid = 0
    datetime_current = datetime.datetime.today()
    year = datetime_current.year
    month = datetime_current.month
    part = str(month) + "/" + str(year)
    total_paid = general_methods.monthlyTotalPaidByDate(str(month), str(year))
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
        total_object = TotalOrderObject(profile=None, total_price=0, earning=0, is_paid=False, paid_date=None)
        total_object.profile = user
        total_object.earning = total_earning
        total_object.total_price = general_methods.monthlyMemberOrderTotal(user, )
        payment = earningPayments.objects.filter(profile=user,
                                                 payedDate=part)
        if payment.count() > 0:
            total_object.is_paid = True
            total_object.paid_date = payment[0].creationDate

        earningArray.append(total_object)

    for key in earnDict:
        total = total + float(earnDict[key])

    if request.method == 'POST':
        userprofile = Profile.objects.filter(user__is_active=True)
        earnDict = dict()
        earningArray = []
        total = 0
        total_paid = 0
        not_paid = 0

        total_paid = general_methods.monthlyTotalPaidByDate(request.POST['ay'], request.POST['yil'])

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
            total_object = TotalOrderObject(profile=None, total_price=0, earning=0, is_paid=False, paid_date=None)
            total_object.profile = user
            total_object.earning = total_earning
            total_object.total_price = general_methods.monthlyMemberOrderTotalByDate(user, int(request.POST['ay']),
                                                                                     int(request.POST['yil']))
            payment = earningPayments.objects.filter(profile=user,
                                                     payedDate=request.POST['ay'] + "/" + request.POST['yil'])
            if payment.count() > 0:
                total_object.is_paid = True
                total_object.paid_date = payment[0].creationDate

            earningArray.append(total_object)

        for key in earnDict:
            total = total + float(earnDict[key])

        return render(request, 'kazanclar/odenecekler.html',
                      {"earnDict": earningArray, 'total': total, 'total_paid': total_paid,
                       'not_paid': float(total) - float(total_paid),
                       'part': part, 'month': request.POST['ay'], 'year': request.POST['yil']})

    return render(request, 'kazanclar/odenecekler.html',
                  {"earnDict": earningArray, 'total': total, 'total_paid': total_paid,
                   'not_paid': float(total) - float(total_paid),
                   'part': part, 'month': str(month), 'year': str(year)})


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


@login_required
def make_pay(request):
    if request.POST:
        try:

            profile_id = request.POST.get('profile_id')
            user = request.user
            part = request.POST.get('part')
            payment = request.POST.get('payment')

            payment = earningPayments(profile=Profile.objects.get(id=profile_id),
                                      payer_profile=Profile.objects.get(user=user),
                                      payedDate=part,
                                      paymentTotal=payment)

            payment.save()

            subject, from_email, to = 'INOKS Ödeme Yapıldı', 'ik@oxityazilim.com', payment.profile.user.email
            text_content = 'Sayın ' + payment.profile.user.first_name + ' ' + payment.profile.user.last_name + '<br>'
            html_content = payment.payedDate + ' dönemine ait' + payment.paymentTotal + ' ₺ ödemeiniz yapılmıştır.'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})

        except Exception as e:

            return JsonResponse({'status': 'Fail', 'msg': e})

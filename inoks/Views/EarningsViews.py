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
    return render(request, 'kazanclar/odenecekler.html')



def calculate_earning(request):
    userprofile = Profile.objects.filter(user__is_active=True)

    for user in userprofile:

        profileArray = []
        levelDict = dict()
        level = 1
        total_earning = 0

        profileArray.append(user.id)

        general_methods.returnLevelTree(profileArray, levelDict, level)

        for i in range(7):
            total_earning = float(total_earning) + float(general_methods.calculate_earning(levelDict, i + 1))







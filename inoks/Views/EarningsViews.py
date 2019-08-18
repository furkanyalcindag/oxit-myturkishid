from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from inoks.models import Order, Profile


@login_required
def return_my_earnings_report(request):
    current_user = request.user
    userprofile = Profile.objects.get(user=current_user)

    total_my_orders = Order.objects.filter(isApprove=True,profile_id=userprofile.id).count()
    orders = Order.objects.filter(isApprove=True, profile_id=userprofile.id)
    return render(request, 'kazanclar/kazanclarim.html', {'orders': orders, 'total_my_orders': total_my_orders})


@login_required
def return_all_earnings_report(request):
    total_my_orders = Order.objects.filter(isApprove=True).count()
    orders = Order.objects.filter(isApprove=True)

    return render(request, 'kazanclar/kazanclar.html', {'orders': orders, 'total_my_orders': total_my_orders})

import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from inoks import tasks
from inoks.models import Profile, Product, Order
from inoks.serializers.order_serializers import OrderSerializer
from inoks.serializers.profile_serializers import ProfileSerializer
from inoks.services.general_methods import activeUser, activeOrder


@login_required
def return_admin_dashboard(request):
    today = datetime.date.today()
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    last_week = today - datetime.timedelta(days=7)
    last_month = (today - datetime.timedelta(days=30))
    last_three_month = (today - datetime.timedelta(days=90))
    last_year = (today - datetime.timedelta(days=365))
    total_user = Profile.objects.count()
    total_product = Product.objects.count()
    total_order = Order.objects.count()
    users = Profile.objects.filter(isApprove=False)
    pending_orders = Order.objects.filter(isApprove=False)
    daily_user = Profile.objects.filter(creationDate__range=(today_min, today_max)).count()
    weekly_user = Profile.objects.filter(creationDate__gte=last_week).count()
    last_months_user = Profile.objects.filter(creationDate__gte=last_month).count()
    last_three_months_user = Profile.objects.filter(creationDate__gte=last_three_month).count()
    yearly_user = Profile.objects.filter(creationDate__gte=last_year).count()
    orders = Order.objects.filter(isApprove=True).order_by('-creationDate')[:6]

    return render(request, 'dashboard/admin-dashboard.html',
                  {'total_user': total_user, 'total_product': total_product, 'total_order': total_order,
                   'pending_orders': pending_orders, 'users': users, 'weekly_user': weekly_user,
                   'daily_user': daily_user, 'last_months_user': last_months_user,
                   'last_three_months_user': last_three_months_user, 'yearly_user': yearly_user, 'orders': orders})


@login_required
def return_user_dashboard(request):
    current_user = request.user
    userprofile = Profile.objects.get(user=current_user)
    orders = Order.objects.filter(isApprove=True, profile_id=userprofile.id)
    my_orders = Order.objects.filter(isApprove=True, profile_id=userprofile.id).count()
    return render(request, 'dashboard/user-dashboard.html',
                  {'my_orders': my_orders, 'orders': orders})


@api_view()
def getPendingProfile(request, pk):
    profile = Profile.objects.filter(pk=pk)

    data = ProfileSerializer(profile, many=True)

    responseData = {}
    responseData['profile'] = data.data
    responseData['profile'][0]
    return JsonResponse(responseData, safe=True)


@login_required
def pending_profile_delete(request, pk):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Profile.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except Profile.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def profile_active_passive(request):
    if request.POST:
        try:

            user_id = request.POST.get('user_id')

            activeUser(request, int(user_id))

            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})

        except Exception as e:

            return JsonResponse({'status': 'Fail', 'msg': e})


@login_required
def pending_order_delete(request, pk):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Order.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except Order.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@api_view()
def getPendingOrder(request, pk):
    order = Order.objects.filter(pk=pk)

    data = OrderSerializer(order, many=True)

    responseData = {}
    responseData['pending_order'] = data.data
    responseData['pending_order'][0]
    return JsonResponse(responseData, safe=True)


@login_required
def pendingOrderActive(request):
    if request.POST:
        try:

            user_id = request.POST.get('user_id')

            activeOrder(request, int(user_id))

            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})

        except Exception as e:

            return JsonResponse({'status': 'Fail', 'msg': e})


@api_view()
def getMyOrder(request, pk):
    tasks.demo_task("hdsds")
    order = Order.objects.filter(pk=pk)

    data = OrderSerializer(order, many=True)

    responseData = {}
    responseData['order'] = data.data
    responseData['order'][0]
    return JsonResponse(responseData, safe=True)

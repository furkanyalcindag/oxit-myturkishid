from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from inoks.Forms.OrderForm import OrderForm
from inoks.Forms.OrderSituationsForm import OrderSituationsForm
from inoks.models import Order, OrderSituations, Profile
from inoks.serializers.order_serializers import OrderSerializer
from inoks.services.general_methods import activeOrder


@login_required
def return_add_orders(request):
    order_form = OrderForm();
    if request.method == 'POST':

        order_form = OrderForm(request.POST)

        if order_form.is_valid():

            order = Order(profile=order_form.cleaned_data['profile'],

                          quantity=order_form.cleaned_data['quantity'],
                          city=order_form.cleaned_data['city'],
                          district=order_form.cleaned_data['district'],
                          sponsor=order_form.cleaned_data['sponsor'],
                          address=order_form.cleaned_data['address'],
                          payment_type=order_form.cleaned_data['payment_type'],
                          isContract=order_form.cleaned_data['isContract'])

            order.save()

            order.product.add(order_form.cleaned_data['product'])

            order.order_situations.add(order_form.cleaned_data['order_situations'])

            order.save()

            return redirect('inoks:siparis-ekle')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'siparisler/siparis-ekle.html', {'order_form': order_form})


@login_required
def return_pending_orders(request):
    pending_orders = Order.objects.filter(isApprove=False)

    return render(request, 'siparisler/bekleyen-siparisler.html', {'pending_orders': pending_orders})


@login_required
def return_orders(request):
    orders = Order.objects.filter(isApprove=True)
    return render(request, 'siparisler/siparisler.html', {'orders': orders})


@login_required
def return_order_situations(request):
    order_situations_form = OrderSituationsForm();

    if request.method == 'POST':

        order_situations_form = OrderSituationsForm(request.POST)

        if order_situations_form.is_valid():

            orderSituations = OrderSituations(name=order_situations_form.cleaned_data['name'])

            orderSituations.save()

            return redirect('inoks:siparis-durumlari')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')
    order_situations = OrderSituations.objects.all()
    return render(request, 'siparisler/siparis-durumlari.html',
                  {'order_situations_form': order_situations_form, 'order_situations': order_situations})


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


@login_required
def return_my_orders(request):
    current_user = request.user
    userprofile = Profile.objects.get(user=current_user)
    orders = Order.objects.filter(isApprove=True, profile_id=userprofile.id)
    return render(request, 'siparisler/siparislerim.html', {'orders': orders})


@api_view()
def getMyOrder(request, pk):
    order = Order.objects.filter(pk=pk)

    data = OrderSerializer(order, many=True)

    responseData = {}
    responseData['order'] = data.data
    responseData['order'][0]
    return JsonResponse(responseData, safe=True)

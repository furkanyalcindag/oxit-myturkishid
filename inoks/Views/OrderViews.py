import json
import pickle

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from inoks.Forms.OrderForm import OrderForm
from inoks.Forms.OrderFormAdmin import OrderFormAdmin
from inoks.Forms.OrderSituationsForm import OrderSituationsForm
from inoks.models import Order, OrderSituations, Profile, Product, OrderProduct
from inoks.models.CartObject import CartObject
from inoks.models.OrderObject import OrderObject
from inoks.serializers.order_serializers import OrderSerializer
from inoks.serializers.product_cart_serializer import CartSerializer
from inoks.services import general_methods
from inoks.services.general_methods import activeOrder



@login_required
def return_add_orders_admin(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    order_form = OrderFormAdmin(instance=Profile.objects.get(user=request.user))
    products = Product.objects.all()
    current_user = request.user
    profile = Profile.objects.get(user=current_user)

    if request.method == 'POST':

        order_form = OrderForm(request.POST)

        if order_form.is_valid():

            total_price = 0

            products_quantity = order_form.cleaned_data['droptxt']

            products_quantity = products_quantity.split(',')


            order = Order(profile=order_form.cleaned_data['profile'],

                          city=order_form.cleaned_data['city'],
                          district=order_form.cleaned_data['district'],

                          address=order_form.cleaned_data['address'],
                          payment_type=order_form.cleaned_data['payment_type'],
                          isContract=order_form.cleaned_data['isContract'], otherAddress=request.POST['diger_adres'],
                          companyInfo=request.POST['kurumsal_bilgi'])
            order.isContract = order_form.cleaned_data['isContract']
            order.save()

            for products_q in products_quantity:
                product = products_q.split('x')
                prod = Product.objects.get(id=int(product[1].strip()))
                orderProduct = OrderProduct(order=order, product=prod,
                                            quantity=int(product[0].strip()))
                orderProduct.save()

                total_price = total_price + (int(product[0].strip()) * prod.price)

            order.totalPrice = total_price
            order.save()

            # order.product.add(order_form.cleaned_data['product'])

            order.order_situations.add(OrderSituations.objects.get(name='Ödeme Bekliyor'))

            order.save()

            messages.success(request, 'Sipariş başarıyla eklendi.')
            return redirect('inoks:siparis-ekle')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'siparisler/siparis-ekle.html',
                  {'order_form': order_form, 'products': products, 'profile': profile})

@login_required
def return_add_orders(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    order_form = OrderForm(instance=Profile.objects.get(user=request.user))
    products = Product.objects.all()
    current_user = request.user
    profile = Profile.objects.get(user=current_user)

    if request.method == 'POST':

        order_form = OrderForm(request.POST)

        if order_form.is_valid():

            total_price = 0

            products_quantity = order_form.cleaned_data['droptxt']

            products_quantity = products_quantity.split(',')

            order = Order(profile=profile,

                          city=order_form.cleaned_data['city'],
                          district=order_form.cleaned_data['district'],

                          address=order_form.cleaned_data['address'],
                          payment_type=order_form.cleaned_data['payment_type'],
                          isContract=order_form.cleaned_data['isContract'], otherAddress=request.POST['diger_adres'],
                          companyInfo=request.POST['kurumsal_bilgi'])
            order.isContract = order_form.cleaned_data['isContract']
            order.save()

            for products_q in products_quantity:
                product = products_q.split('x')
                prod = Product.objects.get(id=int(product[1].strip()))
                orderProduct = OrderProduct(order=order, product=prod,
                                            quantity=int(product[0].strip()))
                orderProduct.save()

                total_price = total_price + (int(product[0].strip()) * prod.price)

            order.totalPrice = total_price
            order.save()

            # order.product.add(order_form.cleaned_data['product'])

            order.order_situations.add(OrderSituations.objects.get(name='Ödeme Bekliyor'))

            order.save()

            messages.success(request, 'Sipariş başarıyla eklendi.')
            return redirect('inoks:siparis-ekle')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'siparisler/siparis-ekle.html',
                  {'order_form': order_form, 'products': products, 'profile': profile})


@login_required
def return_add_orders_from_cart(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    order_form = OrderForm()
    products = Product.objects.all()
    current_user = request.user
    profile = Profile.objects.get(user=current_user)

    myDict = dict(request.GET)
    urun_miktar = []
    urun_miktar_2 = []
    myDict2 = dict()

    for key in myDict:
        if key.startswith('cust'):
            pickup_dict = dict()
            x = myDict[key][0].split("&")
            x = CartObject(product_id=x[0], quantity=x[1])
            urun_miktar.append(x)
            pickup_dict['product_id'] = x.product_id
            pickup_dict['quantity'] = x.quantity
            urun_miktar_2.append(pickup_dict)

    myDict2['deneme'] = urun_miktar
    serializer = CartSerializer(urun_miktar, many=True)
    data = json.dumps(serializer.data)
    # data = serializers.serialize('json', myDict2)
    # serializer = CartSerializer(urun_miktar, many=True)

    # data = serializer.data

    if request.method == 'POST':

        order_form = OrderForm(request.POST)

        if order_form.is_valid():

            total_price = 0

            products_quantity = order_form.cleaned_data['droptxt']

            products_quantity = products_quantity.split(',')

            order = Order(profile=profile,

                          city=order_form.cleaned_data['city'],
                          district=order_form.cleaned_data['district'],

                          address=order_form.cleaned_data['address'],
                          payment_type=order_form.cleaned_data['payment_type'],
                          isContract=order_form.cleaned_data['isContract'], otherAddress=request.POST['diger_adres'],
                          companyInfo=request.POST['kurumsal_bilgi'])
            order.isContract = order_form.cleaned_data['isContract']
            order.save()

            for products_q in products_quantity:
                product = products_q.split('x')
                prod = Product.objects.get(id=int(product[1].strip()))
                orderProduct = OrderProduct(order=order, product=prod,
                                            quantity=int(product[0].strip()))
                orderProduct.save()

                total_price = total_price + (int(product[0].strip()) * prod.price)

            order.totalPrice = total_price
            order.save()

            # order.product.add(order_form.cleaned_data['product'])

            order.order_situations.add(OrderSituations.objects.get(name='Ödeme Bekliyor'))

            order.save()

            messages.success(request, 'Sipariş başarıyla eklendi.')
            return redirect('inoks:siparis-ekle')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'siparisler/siparis-ekle.html',
                  {'order_form': order_form, 'products': products, 'product_array': data, 'profile': profile})


@login_required
def return_pending_orders(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    pending_orders = Order.objects.filter(isApprove=False)

    return render(request, 'siparisler/bekleyen-siparisler.html', {'pending_orders': pending_orders})


@login_required
def return_orders(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    orders = Order.objects.filter(isApprove=True).order_by('-id')

    order_situations = OrderSituations.objects.all()
    return render(request, 'siparisler/siparisler.html', {'orders': orders, 'order_situations': order_situations})


@login_required
def return_order_situations(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    order_situations_form = OrderSituationsForm()

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
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    current_user = request.user
    userprofile = Profile.objects.get(user=current_user)
    orderss = Order.objects.filter(profile_id=userprofile.id)

    orders = []

    for order in orderss:
        orderObject = OrderObject(order=order, total_price=0)

        orderObject.total_price = order.totalPrice
        orders.append(orderObject)

    return render(request, 'siparisler/siparislerim.html', {'orders': orderss})


@api_view()
def getMyOrder(request, pk):
    order = Order.objects.filter(pk=pk)

    data = OrderSerializer(order, many=True)

    responseData = {}
    responseData['order'] = data.data
    responseData['order'][0]
    return JsonResponse(responseData, safe=True)


@login_required
def orders_delete(request, pk):
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
def getOrder(request, pk):
    order = Order.objects.filter(pk=pk)

    data = OrderSerializer(order, many=True)

    responseData = {}
    responseData['order'] = data.data
    responseData['order'][0]
    return JsonResponse(responseData, safe=True)


@api_view(http_method_names=['POST'])
def siparis_durumu_guncelle(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    try:
        isExist = False
        adSoyad = ''
        order_id = request.POST['order_id']
        situation_id = request.POST['situation_id']
        situation = OrderSituations.objects.get(pk=situation_id)
        order = Order.objects.get(pk=order_id)

        if len(order.order_situations.filter(name=situation.name)) > 0:
            order.order_situations.remove(situation)
            order.save()

        order.order_situations.add(situation)
        order.save()

        subject, from_email, to = 'BAVEN Sipariş Durumunuz Güncellendi ', 'ik@oxityazilim.com', order.profile.user.email
        text_content = order_id +'numaralı sipariş durumunuz güncellendi.'
        html_content = '<p> <strong>Site adresi:</strong> <a href="http://www.smutekgrup.com"></a>www.mutekgrup.com</p>'
        html_content = html_content + '<p><strong>Yeni Sipariş Durumu: </strong> ' + situation.name + '</p>'

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return JsonResponse({'status': 'Success', 'msg': 'Sipariş durumu güncellendi'})

    except Exception as e:

        return JsonResponse({'status': 'Fail', 'msg': 'Sipariş durumu güncellenmedi'})

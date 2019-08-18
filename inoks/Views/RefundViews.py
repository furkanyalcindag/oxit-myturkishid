from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from inoks.Forms.RefundForm import RefundForm
from inoks.Forms.RefundSituationsForm import RefundSituationsForm
from inoks.models import Refund
from inoks.models.RefundSituations import RefundSituations


@login_required
def return_add_refund(request):
    refund_form = RefundForm()

    if request.method == 'POST':

        refund_form = RefundForm(request.POST, request.FILES)

        if refund_form.is_valid():

            refund = Refund(order=refund_form.cleaned_data['order'],
                            product=refund_form.cleaned_data['product'],
                            profile=refund_form.cleaned_data['profile'],
                            orderQuantity=refund_form.cleaned_data['orderQuantity'],
                            isOpen=refund_form.cleaned_data['isOpen'])

            refund.save()

            refund.refundSituations.add(refund_form.cleaned_data['refundSituations'])

            refund.save()

            return redirect('inoks:iadeler')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'iadeler/iade-olustur.html', {'refund_form': refund_form})


@login_required
def return_refunds(request):
    refund_list = Refund.objects.all()
    return render(request, 'iadeler/iadeler.html', {'refund_list': refund_list})


@login_required
def return_refund_situations(request):
    refund_situations_form = RefundSituationsForm();

    if request.method == 'POST':

        refund_situations_form = RefundSituationsForm(request.POST)

        if refund_situations_form.is_valid():

            refundSituations = RefundSituations(name=refund_situations_form.cleaned_data['name'])

            refundSituations.save()

            return redirect('inoks:iade-durumlari')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')
    situations = RefundSituations.objects.all()
    return render(request, 'iadeler/iade-durumlari.html',
                  {'refund_situations_form': refund_situations_form, 'situations': situations})


@login_required
def refund_situations_delete(request, pk):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = RefundSituations.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except RefundSituations.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def refund_situations_update(request, pk):
    refundSituations = RefundSituations.objects.get(id=pk)
    refund_situations_form = RefundSituationsForm(request.POST or None, instance=refundSituations)

    if refund_situations_form.is_valid():
        refund_situations_form.save()
        messages.warning(request, 'Başarıyla Güncellendi')
        redirect('inoks:iade-durumlari')
    else:
        messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'iadeler/iade-durumlari.html', {'refund_situations_form': refund_situations_form})

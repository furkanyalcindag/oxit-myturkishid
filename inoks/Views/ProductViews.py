from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.decorators import api_view

from inoks.Forms.ImageForm import ImageForm
from inoks.Forms.ProductCategoryForm import ProductCategoryForm
from inoks.Forms.ProductForm import ProductForm
from inoks.models import Product, ProductCategory
from inoks.models.ProductImage import ProductImage
from inoks.serializers.product_serializers import ProductSerializer


@login_required
def return_add_products(request):
    product_form = ProductForm()

    # image_form = modelformset_factory(ProductImage,
    #                                 form=ImageForm, extra=4)
    durum = "EKLE"

    if request.method == 'POST':

        product_form = ProductForm(request.POST, request.FILES)

        # image_form = image_form(request.POST, request.FILES,
        # queryset=ProductImage.objects.none())

        if product_form.is_valid():

            product = Product(
                name=product_form.cleaned_data['name'],
                price=product_form.cleaned_data['price'],

                stock=product_form.cleaned_data['stock'],

                info=product_form.cleaned_data['info'])

            product.save()

            for f in request.FILES.getlist('input2[]'):
                productImages = ProductImage(productImage=f)
                productImages.save()
                product.productImage.add(productImages)

            product.save()

            for category in product_form.cleaned_data['category']:
                product.category.add(category)

            product.save()

            messages.success(request, 'Ürün Kaydedildi.')

            return redirect('inoks:urunler')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'urunler/urun-ekle.html',
                  {'product_form': product_form, 'durum': durum})


@login_required
def product_delete(request, pk):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Product.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except Product.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def productCategory_delete(request, pk):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = ProductCategory.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except Product.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def productCategory_update(request, pk):
    productCategory = ProductCategory.objects.get(id=pk)
    product_category_form = ProductCategoryForm(request.POST or None, instance=productCategory)

    if product_category_form.is_valid():
        product_category_form.save()
        messages.warning(request, 'Başarıyla Güncellendi')
        return redirect('inoks:urun-kategori-ekle')
    else:
        messages.warning(request, 'Alanları Kontrol Ediniz')
    categories = ProductCategory.objects.all()
    return render(request, 'urunler/urun-kategori-ekle.html',
                  {'product_category_form': product_category_form, 'categories': categories})


@login_required
def product_update(request, pk):
    product = Product.objects.get(id=pk)
    product_form = ProductForm(request.POST or None, instance=product)
    durum = "GUNCELLE"
    images = product.productImage.all()

    if request.method == 'POST':
        if product_form.is_valid():
            product.category.clear()
            for category in product_form.cleaned_data['category']:
                product.category.add(category)

            product.save()

            messages.warning(request, 'Başarıyla Güncellendi')

            return redirect('inoks:urun-listesi')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'urunler/urun-ekle.html', {'product_form': product_form, 'durum': durum, 'images':images})


@api_view()
def getProduct(request, pk):
    product = Product.objects.filter(pk=pk)

    data = ProductSerializer(product, many=True)

    responseData = {}
    responseData['product'] = data.data
    responseData['product'][0]
    return JsonResponse(responseData, safe=True)


@api_view()
def getProducts(request, pk):
    product = Product.objects.filter(pk=pk)

    data = ProductSerializer(product, many=True)

    responseData = {}
    responseData['product'] = data.data
    responseData['product'][0]
    return JsonResponse(responseData, safe=True)


@login_required
def return_product_list(request):
    product_list = Product.objects.all()
    return render(request, 'urunler/urun-listesi.html', {'product_list': product_list})


@login_required
def return_cleaning_products(request):
    products = Product.objects.filter(category=1)
    return render(request, 'urunler/genel-temizlik-urunleri.html', {'products': products})


@login_required
def return_health_products(request):
    products = Product.objects.filter(category=2)
    return render(request, 'urunler/organik-temizlik-urunleri.html', {'products': products})


@login_required
def return_automotive_products(request):
    products = Product.objects.filter(category=3)
    return render(request, 'urunler/arac-temizlik-urunleri.html', {'products': products})


@login_required
def return_products(request):
    genel = Product.objects.filter(category=1)
    organik = Product.objects.filter(category=2)
    urunler = Product.objects.all()
    return render(request, 'urunler/urunler.html', {'genel': genel, 'organik': organik, 'urunler': urunler})


@login_required
def return_add_product_category(request):
    product_category_form = ProductCategoryForm();

    if request.method == 'POST':

        product_category_form = ProductCategoryForm(request.POST)

        if product_category_form.is_valid():

            productCategory = ProductCategory(name=product_category_form.cleaned_data['name'])

            productCategory.save()

            return redirect('inoks:urun-kategori-ekle')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')
    categories = ProductCategory.objects.all()
    return render(request, 'urunler/urun-kategori-ekle.html',
                  {'product_category_form': product_category_form, 'categories': categories})

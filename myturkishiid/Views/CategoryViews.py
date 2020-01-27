
from django.contrib import messages
from django.shortcuts import redirect, render

from myturkishiid.Forms.CategoryDesc import CategoryDescForm
from myturkishiid.Forms.CategoryForm import CategoryForm
from myturkishiid.models import Category

from myturkishiid.models import CategoryDesc
from myturkishiid.models.Language import Language


def category_save(request):
    form_category = CategoryForm(request.POST or None)

    if request.method == 'POST':

        if form_category.is_valid():
            form_category.save()
            messages.success(request, 'Kategori kaydedildi.')

            return redirect('myturkishid:category-save')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'categorytemp/category-save.html', {'form_category': form_category})


def categoryDesc_save(request, pk):
    form_categoryDesc = CategoryDescForm(request.POST)
    category = Category.objects.get(pk=pk)
    categoryDesc = CategoryDesc.objects.filter(category=category)
    lang = Language.objects.all()

    if request.method == 'POST':

        if form_categoryDesc.is_valid():
            form = form_categoryDesc.save(commit=False)
            form.category = category
            form.save()
            messages.success(request, 'Kategori Kaydedildi.')

            return redirect('myturkishid:categoryDesc-save', pk)

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'categorytemp/categoryDesc-save.html',
                  {'form_category': form_categoryDesc, 'category': category, 'lang': lang, 'catDescs': categoryDesc})


def get_category(request):
    category = Category.objects.all()

    return render(request, 'categorytemp/get-category.html', {'category': category})

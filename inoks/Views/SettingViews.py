from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def return_profil_settings(request):
    return render(request, 'ayarlar/profil-ayarlari.html')

@login_required
def return_system_settings(request):
    return render(request, 'ayarlar/sistem-ayarlari.html')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def return_create_report(request):
    return render(request, 'raporlar/rapor-olustur.html')
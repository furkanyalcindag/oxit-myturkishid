from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth, messages

# Create your views here.
from inoks.models import Profile


def index(request):
    return render(request, 'accounts/index.html')


# def login(request):
# return render(request, 'registration/login.html')


def login(request):
    if request.user.is_authenticated is True:
        return redirect('inoks:admin-dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            # return render(request, 'patient/:patient/index', context={})
            return redirect('inoks:admin-dashboard')

        else:
            messages.add_message(request, messages.SUCCESS, 'Mail Adresi Ve Şifre Uyumsuzluğu')
            return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')


def forgot(request):
    return render(request, 'registration/forgot-password.html')


def pagelogout(request):
    logout(request)
    return redirect('accounts:login')

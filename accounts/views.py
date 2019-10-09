from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
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

            if user.groups.all()[0].name == 'Admin':
                return redirect('inoks:admin-dashboard')

            elif user.groups.all()[0].name == 'Üye':
                return redirect('inoks:user-dashboard')

            else:
                return redirect('accounts:logout')

        else:
            messages.add_message(request, messages.SUCCESS, 'Mail Adresi Ve Şifre Uyumsuzluğu')
            return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')


def forgot(request):
    if request.method == 'POST':
        mail = request.POST.get('username')
        obj = User.objects.filter(username=mail)
        if obj.count() != 0:
            obj = obj[0]
            password = User.objects.make_random_password()
            obj.set_password(password)
            # form.cleaned_data['password'] = make_password(form.cleaned_data['password'])
            user = obj.save()
            html_content = ''
            subject, from_email, to = 'BAVEN Kullanıcı Bilgileri', 'no-reply@baven.com', obj.email
            text_content = 'Aşağıda ki bilgileri kullanarak sisteme giriş yapabilirsiniz.'
            html_content = '<p> <strong>Site adresi:</strong> <a href="http://185.122.203.112/"></a>baven.com</p>'
            html_content = html_content + '<p><strong>Kullanıcı Adı:</strong>' + obj.username + '</p>'
            html_content = html_content + '<p><strong>Şifre:</strong>' + password + '</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, "Giriş bilgileriniz mail adresinize gönderildi. ")
            return redirect("accounts:login")
        else:
            messages.warning(request, "Geçerli bir mail adresi giriniz.")
            return redirect("accounts:forgot")

    return render(request, 'registration/forgot.html')



def pagelogout(request):
    logout(request)
    return redirect('accounts:login')

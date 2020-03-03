from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render

from myturkishiid.Forms.ProfileForm import ProfileForm
from myturkishiid.Forms.ProfileUpdateForm import ProfileUpdateForm
from myturkishiid.Forms.UserForm import UserForm
from myturkishiid.Forms.UserUpdateForm import UserUpdateForm
from myturkishiid.models.Profile import Profile
from myturkishiid.services import general_methods


@login_required
def return_add_users(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    user_form = UserForm()
    profile_form = ProfileForm()

    if request.method == 'POST':
        x = User.objects.latest('id')

        data = request.POST.copy()
        data['username'] = data['email']
        user_form = UserForm(data)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save(commit=False)
            group = Group.objects.get(name='Üye')
            user2 = user_form.save()
            password = User.objects.make_random_password()
            user.set_password(password)
            user2.groups.add(group)

            user.save()

            profil = Profile(user=user,
                             mobilePhone=profile_form.cleaned_data['mobilePhone'],
                             )

            profil.save()

            subject, from_email, to = 'MyTurkish ID Kullanıcı Giriş Bilgileri', 'invest@myturkishid.com', user2.email
            text_content = 'Aşağıda ki bilgileri kullanarak sisteme giriş yapabilirsiniz.'
            html_content = '<p> <strong>Site adresi:</strong> <a href="http://estate.myturkishid.ir/manager/">estate.myturkishid.ir</a></p>'
            html_content = html_content + '<p><strong>Kullanıcı Adı: </strong>' + user2.username + '</p>'
            html_content = html_content + '<p><strong>Şifre: </strong>' + password + '</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, 'Üye Başarıyla Kayıt Edilmiştir.')

            return redirect('myturkishid:uyelerim')

        else:
            isExist = general_methods.existMail(data['email'])
            if isExist:
                messages.warning(request, 'Mail adresi başka bir üyemiz tarafından kullanılmaktadır.')

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'user/kullanici-ekle.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def users_update(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')

    user = User.objects.get(id=pk)
    user_form = UserUpdateForm(request.POST or None, instance=user)
    profile = Profile.objects.get(user=user)
    profile_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=profile)

    if request.method == 'POST':

        if user_form.is_valid() and profile_form.is_valid():

            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            user.email = user_form.cleaned_data['email']
            user.username = user_form.cleaned_data['email']
            user.save()
            profile_form.save()

            messages.success(request, 'Profil Bilgileriniz Başarıyla Güncellenmiştir.')
            return redirect('myturkishid:uyelerim')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'user/kullanici-ekle.html',
                  {'user_form': user_form, 'profile_form': profile_form, })


@login_required
def return_my_users(request):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    users = Profile.objects.all()

    return render(request, 'user/uyelerim.html', {'users': users})


@login_required
def user_delete(request, pk):
    perm = general_methods.control_access(request)

    if not perm:
        logout(request)
        return redirect('accounts:login')
    user = User.objects.get(pk=pk)
    profile = Profile.objects.get(user=user)
    profile.delete()
    user.delete()
    messages.warning(request, 'Üye Silindi')

    return redirect('myturkishid:uyelerim')

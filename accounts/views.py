from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.contrib import auth, messages

# Create your views here.
from inoks.Forms.ProfileFormForMember import ProfileForm
from education.Forms.UserForm import UserForm
from inoks.models import Profile
from inoks.services import general_methods


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


def register_member(request):
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

            profil = Profile(user=user, tc=profile_form.cleaned_data['tc'],
                             profileImage=profile_form.cleaned_data['profileImage'],
                             address=profile_form.cleaned_data['address'],
                             gender=profile_form.cleaned_data['gender'],
                             job=profile_form.cleaned_data['job'],
                             city=profile_form.cleaned_data['city'],
                             educationLevel=profile_form.cleaned_data['educationLevel'],
                             mobilePhone=profile_form.cleaned_data['mobilePhone'],
                             birthDate=profile_form.cleaned_data['birthDate'],
                             district=profile_form.cleaned_data['district'],
                             sponsor=profile_form.cleaned_data['sponsor'])
            profil.sponsor = profile_form.cleaned_data['sponsor']
            profil.isContract = profile_form.cleaned_data['isContract']
            sponsorNumber = Profile.objects.filter(sponsor=profile_form.cleaned_data['sponsor']).count()
            sp_profile=Profile.objects.get(pk=profile_form.cleaned_data['sponsor'].pk)
            limit = 0

            if sp_profile.user.groups.all()[0].name  == 'Admin':
                limit = 9
            else:
                limit = 2

            if sponsorNumber > limit:
                messages.warning(request, 'Üyeye Sponsor Eklenemez. Sponsor Alanı Dolmuştur.')
                return redirect('accounts:register')
            else:
                profil.save()

                subject, from_email, to = 'INOKS Kullanıcı Giriş Bilgileri', 'ik@oxityazilim.com', user2.email
                text_content = 'Aşağıda ki bilgileri kullanarak sisteme giriş yapabilirsiniz.'
                html_content = '<p> <strong>Site adresi:</strong> <a href="http://www.smutekgrup.com"></a>www.mutekgrup.com</p>'
                html_content = html_content + '<p><strong>Kullanıcı Adı: </strong>' + user2.username + '</p>'
                html_content = html_content + '<p><strong>Şifre: </strong>' + password + '</p>'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                messages.success(request, 'Üye Başarıyla Kayıt Edilmiştir.')

                return redirect('accounts:login')

        else:
            isExist = general_methods.existMail(data['email'])
            if isExist:
                messages.warning(request, 'Mail adresi başka bir üyemiz tarafından kullanılmaktadır.')

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form})

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from education.Forms.UserForm import UserForm
from inoks.Forms.ProfileForm import ProfileForm
from inoks.models import Profile
from inoks.serializers.profile_serializers import ProfileSerializer
from inoks.services.general_methods import activeUser, passiveUser, reactiveUser


@login_required
def return_add_users(request):
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
            user.set_password("oxit2016")
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
            sponsorNumber = Profile.objects.filter(sponsor=profile_form.cleaned_data['sponsor']).count()

            if sponsorNumber > 2:
                messages.warning(request, 'Üyeye Sponsor Eklenemez. Sponsor Alanı Dolmuştur.')
                return redirect('inoks:kullanici-ekle')
            else:
                profil.save()
                messages.success(request, 'Üye Başarıyla Kayıt Edilmiştir.')

                return redirect('inoks:kullanici-ekle')

        else:

            messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'kullanici/kullanici-ekle.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def users_update(request, pk):
    current_user = request.user
    user = User.objects.get(id=current_user.id)

    user_form = UserForm(request.POST or None, instance=user)
    profile = Profile.objects.get(user=current_user)
    profile_form = ProfileForm(request.POST or None, instance=profile)

    if user_form.is_valid() and profile_form.is_valid():

        profile.save()

        messages.warning(request, 'Başarıyla Güncellendi')

        return redirect('inoks:kullanicilar')

    else:

        messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'kullanici/kullanici-ekle.html', {'profile_form': profile_form, 'user_form': user_form})


@login_required
def return_users(request):
    users = Profile.objects.filter(isActive=True)

    return render(request, 'kullanici/kullanicilar.html', {'users': users})


@login_required
def return_my_users(request):
    current_user = request.user
    userprofile = Profile.objects.get(user=current_user)

    users = Profile.objects.filter(isActive=True, sponsor_id=userprofile.id)

    return render(request, 'kullanici/kullanicilar.html', {'users': users})


@login_required
def return_pending_users(request):
    users = Profile.objects.filter(isApprove=False)

    return render(request, 'kullanici/bekleyen-kullanicilar.html', {'users': users})


@api_view()
def getPendingProfile(request, pk):
    profile = Profile.objects.filter(pk=pk)

    data = ProfileSerializer(profile, many=True)

    responseData = {}
    responseData['profile'] = data.data
    responseData['profile'][0]
    return JsonResponse(responseData, safe=True)


@api_view()
def getAllProfile(request, pk):
    profile = Profile.objects.filter(pk=pk)

    data = ProfileSerializer(profile, many=True)

    responseData = {}
    responseData['profile'] = data.data
    responseData['profile'][0]
    return JsonResponse(responseData, safe=True)


@api_view()
def getDeactiveProfile(request, pk):
    profile = Profile.objects.filter(pk=pk)

    data = ProfileSerializer(profile, many=True)

    responseData = {}
    responseData['profile'] = data.data
    responseData['profile'][0]
    return JsonResponse(responseData, safe=True)


@login_required
def profile_active_passive(request):
    if request.POST:
        try:

            user_id = request.POST.get('user_id')

            activeUser(request, int(user_id))

            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})

        except Exception as e:

            return JsonResponse({'status': 'Fail', 'msg': e})


@login_required
def profile_reactive(request):
    if request.POST:
        try:

            user_id = request.POST.get('user_id')

            reactiveUser(request, int(user_id))

            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})

        except Exception as e:

            return JsonResponse({'status': 'Fail', 'msg': e})


@login_required
def profile_passive(request):
    if request.POST:
        try:

            user_id = request.POST.get('user_id')

            passiveUser(request, int(user_id))

            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})

        except Exception as e:

            return JsonResponse({'status': 'Fail', 'msg': e})


@login_required
def pending_profile_delete(request, pk):
    if request.method == 'POST' and request.is_ajax():
        try:
            obj = Profile.objects.get(pk=pk)
            obj.delete()
            return JsonResponse({'status': 'Success', 'messages': 'save successfully'})
        except Profile.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})

    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})


@login_required
def return_deactive_users(request):
    users = Profile.objects.filter(isActive=False, isApprove=True)

    return render(request, 'kullanici/iptal-edilen-kullanicilar.html', {'users': users})

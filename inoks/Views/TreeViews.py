from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from inoks.models import Profile
from inoks.models.ProfileControlObject import ProfileControlObject
from inoks.services import general_methods


@login_required
def return_my_tree(request):
    profilList = []
    current_user = request.user

    userprofile = Profile.objects.get(user=current_user)

    profilList.append(ProfileControlObject(profile=userprofile, is_controlled=False))

    trees = general_methods.rtrnProfileBySponsorID(profilList)



    #trees = Profile.objects.filter(id__gte=userprofile.id)

    return render(request, 'soyagaci/soy-agacim.html', {'trees': trees, 'profile_id': userprofile.id})


@login_required
def return_all_tree(request):
    trees = Profile.objects.all()
    return render(request, 'soyagaci/soy-agaclari.html', {'trees': trees})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from inoks.models import Profile


@login_required
def return_my_tree(request):
    current_user = request.user

    userprofile = Profile.objects.get(user=current_user)

    trees = Profile.objects.all()

    return render(request, 'soyagaci/soy-agacim.html', {'trees': trees, 'profile_id': userprofile.id})


@login_required
def return_all_tree(request):
    trees = Profile.objects.all()
    return render(request, 'soyagaci/soy-agaclari.html', {'trees': trees})

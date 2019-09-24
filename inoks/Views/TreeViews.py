from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from inoks.models import Profile
from inoks.models.ProfileControlObject import ProfileControlObject
from inoks.services import general_methods


@login_required
def return_my_tree(request):
    profilList = []
    current_user = request.user
    total_earning = 0

    userprofile = Profile.objects.get(user=current_user)

    profileArray = []
    levelDict = dict()
    level = 1
    profileArray.append(userprofile.id)

    general_methods.returnLevelTree(profileArray, levelDict, level)

    for i in range(7):
        total_earning = float(total_earning) + float(general_methods.calculate_earning(levelDict, i + 1))

    x = general_methods.calculate_earning(levelDict, 2)

    total_order = general_methods.monthlyMemberOrderTotal(userprofile)['total_price']

    if total_order is None:
        total_order = 0

    total_order = str(float(str(total_order).replace(",", ".")))

    total = 0

    profilList.append(ProfileControlObject(profile=userprofile, is_controlled=False,
                                           total_order=total_order))

    trees = general_methods.rtrnProfileBySponsorID(profilList)

    # trees = Profile.objects.filter(id__gte=userprofile.id)

    return render(request, 'soyagaci/soy-agacim.html', {'trees': trees, 'profile_id': userprofile.id})


@login_required
def return_all_tree(request):
    trees = []
    profileArray = []
    levelDict = dict()
    level = 1
    profileArray.append(Profile.objects.get(id=7).id)

    general_methods.returnLevelTree(profileArray, levelDict, level)

    tree1 = Profile.objects.all()

    for prof in tree1:
        total_order = general_methods.monthlyMemberOrderTotal(prof)['total_price']

        if total_order is None:
            total_order = 0

        total_order = str(float(str(total_order).replace(",", ".")))
        trees.append(ProfileControlObject(profile=prof, is_controlled=False,
                                          total_order=total_order))

    return render(request, 'soyagaci/soy-agaclari.html', {'trees': trees})

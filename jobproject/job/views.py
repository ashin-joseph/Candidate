from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def jobIndex(request):
    return render(request,"index.html")

def jobIndividual(request, user_id):
    user = get_object_or_404(User, id=user_id)
    roles = Role.objects.filter(user=user)
    certifications = Certification.objects.filter(user=user)
    hardskills = HardSkill.objects.filter(user=user)
    softskills = SoftSkill.objects.filter(user=user)
    tools = ToolAndTechnology.objects.filter(user=user)
    education = Education.objects.filter(user=user)

    context = {
        'user': user,
        'roles': roles,
        'certifications': certifications,
        'hardskills': hardskills,
        'softskills': softskills,
        'tools': tools,
        'education': education,
    }

    return render(request, "individual_details.html", context)
def jobProfiles(request):
    user = User.objects.all()
    context = {'user': user,}
    return render(request,"profiles.html",context)

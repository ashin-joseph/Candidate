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

    return render(request, "candidateandjobcards copy.html", context)

def jobProfiles(request):
    user_data = User.objects.all()
    user_details = []

    for user in user_data:
        user_roles = Role.objects.filter(user=user)
        user_hardskills = HardSkill.objects.filter(user=user)
        user_details.append({
            'user': user,
            'roles': user_roles,
            'hardskills': user_hardskills
        })

    context = {'user_details': user_details}
    return render(request, "candidate/candidateandjobcards copy.html", context)

def candidateandjob(request):
    user_data = User.objects.all()
    user_details = []

    for user in user_data:
        user_roles = Role.objects.filter(user=user)
        user_hardskills = HardSkill.objects.filter(user=user)
        user_details.append({
            'user': user,
            'roles': user_roles,
            'hardskills': user_hardskills
        })

    context = {'user_details': user_details}
    return render(request, "candidate/candidateandjobcards.html", context)

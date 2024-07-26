from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def jobCards(request):
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
    return render(request, "candidate/copy0.html", context)
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

    return render(request, "candidate/copy.html", context)

def Index(request):
    return render(request,"index.html")

def Trial(request):
    # Get role_id from the request (e.g., GET or POST parameter)
    role_id = request.GET.get('role_id')  # or request.POST.get('role_id') for POST requests

    # Get all candidates
    user_data = SotsCandidate.objects.all()

    # If role_id is provided, filter candidates by role_id
    sots = None
    if role_id:
        sots = get_object_or_404(SotsCandidate, id=role_id)

    for candidate in user_data:
        # Handle tags
        if candidate.tag:
            tags = [tag.strip() for tag in candidate.tag.split(',')]
            formatted_tag = ''.join(f'<li>{t}</li>' for t in tags)
            candidate.tags_formatted = formatted_tag
        else:
            candidate.tags_formatted = ""

        # Handle roles
        if candidate.roles:
            roles = [role.strip() for role in candidate.roles.split(',')]
            formatted_role = ''.join(f'<li>{r}</li>' for r in roles)
            candidate.role_formatted = formatted_role
        else:
            candidate.role_formatted = ""

    context = {
        'user_data': user_data,
        'sots': sots,
    }
    return render(request, "candidate/trial.html", context)

def candidateandjob(request):
    user_data = SotsCandidate.objects.all()

    for i in user_data:
        if i.tag:
            tags = [tag.strip() for tag in i.tag.split(',')]
            formatted_tag = ''.join(f'<li>{t}</li>' for t in tags)
            i.tags_formatted = formatted_tag
        else:
            i.tags_formatted = ""

        if i.roles:
            roles = [role.strip() for role in i.roles.split(',')]
            formatted_role = ''.join(f'<li>{r}</li>' for r in roles)
            i.role_formatted = formatted_role
        else:
            i.role_formatted = ""


    context = {'user_data': user_data,
               'tags_formatted':i.tags_formatted,
               'role_formatted':i.role_formatted,
               }
    return render(request, "candidate/candidateandjobcards.html", context)

def candidateProfile(request, role_id):
    sotscan=SotsCandidate.objects.filter(id=role_id)

    for j in sotscan:
        if j.hard_skills:
            skills = [skill.strip() for skill in j.hard_skills.split(',')]
            formatted_hardskills = ''.join(f'<li>{skill}</li>' for skill in skills)
            j.hard_skills_formatted = formatted_hardskills
        else:
            j.hard_skills_formatted = ""

    for k in sotscan:
        if k.soft_skills:
            skills = [skill.strip() for skill in k.soft_skills.split(',')]
            formatted_softskills = ''.join(f'<li>{skill}</li>' for skill in skills)
            k.soft_skills_formatted = formatted_softskills
        else:
            k.soft_skills_formatted = ""

    for l in sotscan:
        if l.tools:
            skills = [skill.strip() for skill in l.tools.split(',')]
            formatted_tools = ''.join(f'<li>{skill}</li>' for skill in skills)
            l.tools_formatted = formatted_tools
        else:
            l.tools_formatted = ""

    for q in sotscan:
        if q.roles:
            roles = [skill.strip() for skill in q.roles.split(',')]
            formatted_roles = ''.join(f'<li>{skill}</li>' for skill in roles)
            q.roles_formatted = formatted_roles
        else:
            q.roles_formatted = ""

    for w in sotscan:
        if w.educational_summary:
            educational_summary = [skill.strip() for skill in w.educational_summary.split(',')]
            formatted_edu = ''.join(f'<li>{skill}</li>' for skill in educational_summary)
            w.educational_summary = formatted_edu
        else:
            w.educational_summary = ""

    for e in sotscan:
        if e.certifications:
            certi = [skill.strip() for skill in e.certifications.split(',')]
            formatted_certi = ''.join(f'<li>{skill}</li>' for skill in certi)
            e.certifications = formatted_certi
        else:
            e.certifications = ""

    context = {
        'sotscan': sotscan,
        'hard_skills_formatted': j.hard_skills_formatted,
        'soft_skills_formatted': k.soft_skills_formatted,
        'tools_formatted': l.tools_formatted,
        'roles_formatted': q.roles_formatted,
        'educational_summary': w.educational_summary,
        'certifications': e.certifications,
    }


    return render(request,"candidate/CandidateProfile.html", context)

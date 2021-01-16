from django.shortcuts import render

from resume.models import about
from resume.models import experience
from resume.models import project
from resume.models import social


def index(request):
    resume = about.About.objects.all().first()

    socials = social.Social.objects.all()

    pro_experiences = experience.Experience.objects.filter(
        experience_type=experience.PRO
    )
    education_experiences = experience.Experience.objects.filter(
        experience_type=experience.EDU
    )

    projects = project.Project.objects.all()
    progression = project.Project.objects.progression()

    context = {
        "resume": resume,
        "socials": socials,
        "pro_experiences": pro_experiences,
        "education_experiences": education_experiences,
        "projects": {"projects": projects, "progression": progression},
    }

    return render(request, "resume/index.html", context=context)

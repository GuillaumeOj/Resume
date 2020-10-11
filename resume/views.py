from django.shortcuts import render

from resume.models import About
from resume.models import Experience
from resume.models import PathWay
from resume.models import Project
from resume.models import Social


def index(request):
    resume = About.objects.all().first()

    socials = Social.objects.filter(about=resume)

    pro_pathway = PathWay.objects.filter(title="Expérience").first()
    pro_experiences = Experience.objects.filter(about=resume, path=pro_pathway)

    education_pathway = PathWay.objects.filter(title="Formation").first()
    education_experiences = Experience.objects.filter(
        about=resume, path=education_pathway
    )

    projects = Project.objects.filter(about=resume)
    progression = Project.objects.progression(resume)

    context = {
        "resume": resume,
        "socials": socials,
        "pro_experiences": pro_experiences,
        "education_experiences": education_experiences,
        "projects": {"projects": projects, "progression": progression},
    }

    return render(request, "resume/index.html", context=context)

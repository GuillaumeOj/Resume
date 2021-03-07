from django.shortcuts import render

from resume.models import about
from resume.models import portfolio
from resume.models import project
from resume.models import social


def index(request):
    resume = about.About.objects.all().first()

    socials = social.Social.objects.all()

    projects = project.Project.objects.all()
    progression = project.Project.objects.progression()

    portfolio_elements = portfolio.Portfolio.objects.all()

    context = {
        "resume": resume,
        "socials": socials,
        "projects": {"projects": projects, "progression": progression},
        "portfolio": portfolio_elements,
    }

    return render(request, "resume/index.html", context=context)

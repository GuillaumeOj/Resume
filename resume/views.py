from django.shortcuts import render

from resume.models import About
from resume.models import Experience
from resume.models import PathWay
from resume.models import Social


def index(request):
    resume = About.objects.all().first()
    socials = Social.objects.filter(about=resume)
    pro_pathway = PathWay.objects.filter(title="Expérience").first()
    pro_experiences = Experience.objects.filter(about=resume, path=pro_pathway)
    context = {"resume": resume, "socials": socials, "pro_experiences": pro_experiences}

    return render(request, "resume/index.html", context=context)

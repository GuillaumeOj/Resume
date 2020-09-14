from django.shortcuts import render

from resume.models import About
from resume.models import Social


def index(request):
    resume = About.objects.all().first()
    socials = Social.objects.filter(about=resume)
    context = {"resume": resume, "socials": socials}

    return render(request, "resume/index.html", context=context)

from django.shortcuts import render

from resume.models import About


def index(request):
    resume = About.objects.all().first()
    context = {"resume": resume}

    return render(request, "resume/index.html", context=context)

from django.shortcuts import render

from main.models import Redactor


def index(request):
    redactors = Redactor.objects.all()
    context = {"redactors": redactors}
    return render(request, "main/index.html", context)

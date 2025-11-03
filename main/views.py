from django.shortcuts import render


def index(request):
    render(request, "main/index.html")

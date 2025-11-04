from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from main.models import Redactor


def index(request):
    redactors = Redactor.objects.all()
    context = {"redactors": redactors}
    return render(request, "main/index.html", context)


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 10


class RedactorDetailView(generic.DetailView):
    model = Redactor


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = "main:redactor-list"

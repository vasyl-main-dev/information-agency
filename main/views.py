from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from main.forms import RedactorCreationForm, NewsCreationForm
from main.models import Redactor, Newspaper


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
    success_url = reverse_lazy("main:redactor-list")


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("main:redactor-list")


class NewspaperListView(generic.ListView):
    model = Newspaper
    paginate_by = 5


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("main:newspaper-list")


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewsCreationForm
    success_url = reverse_lazy("main:newspaper-list")

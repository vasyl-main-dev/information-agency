from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from main.forms import RedactorCreationForm, NewsCreationForm, NewspaperSearchForm, RedactorSearchForm
from main.models import Redactor, Newspaper


def index(request):
    redactors = Redactor.objects.all()
    context = {"redactors": redactors}
    return render(request, "main/index.html", context)


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username")
        context["search_form"] = RedactorSearchForm(initial={"username": username})
        return context

    def get_queryset(self):
        queryset = Redactor.objects.all()
        username = self.request.GET.get("username")

        if username:
            return queryset.filter(username__icontains=username)
        return queryset


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get("title")

        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("main:newspaper-list")


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewsCreationForm
    success_url = reverse_lazy("main:newspaper-list")

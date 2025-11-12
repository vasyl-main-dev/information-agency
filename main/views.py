from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView


from main.forms import RedactorCreationForm, NewsCreationForm, NewspaperSearchForm, RedactorSearchForm
from main.models import Redactor, Newspaper, Topic


def index(request):
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()

    latest_news = Newspaper.objects.order_by("-published_date")[:5]

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
        "latest_news": latest_news,
    }
    return render(request, "main/index.html", context)


class RedactorListView(ListView):
    model = Redactor
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = RedactorSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.GET.get("username")

        if username:
            queryset = queryset.filter(username__icontains=username)
        return queryset


class RedactorDetailView(DetailView):
    model = Redactor


class RedactorDeleteView(LoginRequiredMixin, DeleteView):
    model = Redactor
    success_url = reverse_lazy("main:redactor-list")

    def dispatch(self, request, *args, **kwargs):
        if self.get_object() != request.user:
            return HttpResponseForbidden("You can delete only your own account!")
        return super().dispatch(request, *args, **kwargs)


class RedactorCreateView(LoginRequiredMixin, CreateView):
    model = Redactor
    form_class = RedactorCreationForm

    def get_success_url(self):
        return self.object.get_absolute_url()


class NewspaperListView(ListView):
    model = Newspaper
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = NewspaperSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = Newspaper.objects.prefetch_related("topics", "publishers")
        title = self.request.GET.get("title")

        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset


class NewspaperDetailView(DetailView):
    model = Newspaper

    def get_queryset(self):
        return Newspaper.objects.prefetch_related("topics", "publishers")


class NewspaperDeleteView(LoginRequiredMixin, DeleteView):
    model = Newspaper
    success_url = reverse_lazy("main:newspaper-list")


class NewspaperCreateView(LoginRequiredMixin, CreateView):
    model = Newspaper
    form_class = NewsCreationForm

    def get_success_url(self):
        return self.object.get_absolute_url()


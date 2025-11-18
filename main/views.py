from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView


from main.forms import (
    RedactorCreationForm,
    NewsCreationForm,
    NewspaperSearchForm,
    RedactorSearchForm,
)
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

    def form_valid(self, form):
        """Видалення власного акаунту"""

        redactor = self.get_object()

        if redactor != self.request.user:
            messages.error(self.request, "❌ You can only delete your own account.")
            return redirect(self.request.META.get("HTTP_REFERER", "/"))

        # Success message (важливо для тесту!)
        messages.success(self.request, "Your account has been deleted.")

        # Видаляємо
        response = super().form_valid(form)

        # Logout
        logout(self.request)

        return response


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

    def dispatch(self, request, *args, **kwargs):
        newspaper = self.get_object()

        # ❗ Лише ті, хто є видавцями, можуть видаляти
        if request.user not in newspaper.publishers.all():
            messages.error(request, "❌ You are not allowed to delete this newspaper.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "🗑 Newspaper was successfully deleted.")
        return super().delete(request, *args, **kwargs)


class NewspaperCreateView(LoginRequiredMixin, CreateView):
    model = Newspaper
    form_class = NewsCreationForm

    def get_success_url(self):
        return self.object.get_absolute_url()

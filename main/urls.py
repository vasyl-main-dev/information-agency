from django.urls import path

from main.views import (
    index,
    RedactorListView,
    RedactorDetailView,
    RedactorDeleteView,
    RedactorCreateView,
    NewspaperListView,
    NewspaperDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path("redactors/<int:pk>/delete/", RedactorDeleteView.as_view(), name="redactor-delete"),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactor-create"),
    path("news/", NewspaperListView.as_view(), name="news-list"),
    path("news/<int:pk>/", NewspaperDetailView.as_view(), name="news-detail"),
]

app_name = "main"

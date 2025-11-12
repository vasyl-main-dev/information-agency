from django.urls import path, include

from main.views import (
    index,
    RedactorListView,
    RedactorDetailView,
    RedactorDeleteView,
    RedactorCreateView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperDeleteView,
    NewspaperCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path(
        "redactors/<int:pk>/delete/",
        RedactorDeleteView.as_view(),
        name="redactor-delete",
    ),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactor-create"),
    path("news/", NewspaperListView.as_view(), name="newspaper-list"),
    path(
        "newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"
    ),
    path(
        "newspapers/<int:pk>/delete",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete",
    ),
    path("newspapers/create", NewspaperCreateView.as_view(), name="newspaper-create"),
]

app_name = "main"

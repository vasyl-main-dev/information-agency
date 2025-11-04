from django.urls import path

from main.views import (
    index,
    RedactorListView,
    RedactorDetailView,
    RedactorDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactor/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path("redactor/<int:pk>/delete/", RedactorDeleteView.as_view(), name="redactor-delete"),
]

app_name = "main"

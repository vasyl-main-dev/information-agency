from django.urls import path

from main import views

# main/urls.py
urlpatterns = [
    path("", views.index, name="index"),
    # Redactors
    path("redactors/", views.RedactorListView.as_view(), name="redactor-list"),
    path(
        "redactors/<int:pk>/",
        views.RedactorDetailView.as_view(),
        name="redactor-detail",
    ),
    path(
        "redactors/<int:pk>/delete/",
        views.RedactorDeleteView.as_view(),
        name="redactor-delete",
    ),
    path(
        "redactors/create/", views.RedactorCreateView.as_view(), name="redactor-create"
    ),
    # Newspapers
    path("newspapers/", views.NewspaperListView.as_view(), name="newspaper-list"),
    path(
        "newspapers/<int:pk>/",
        views.NewspaperDetailView.as_view(),
        name="newspaper-detail",
    ),
    path(
        "newspapers/<int:pk>/delete/",
        views.NewspaperDeleteView.as_view(),
        name="newspaper-delete",
    ),
    path(
        "newspapers/create/",
        views.NewspaperCreateView.as_view(),
        name="newspaper-create",
    ),
]

app_name = "main"

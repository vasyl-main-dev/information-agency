from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main.models import Newspaper, Redactor, Topic


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_filter = ("publishers", "topics")
    list_display = ("title", "published_date")


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("year_of_experience",)
    search_fields = ("username", "first_name", "last_name")
    ordering = ("-year_of_experience",)

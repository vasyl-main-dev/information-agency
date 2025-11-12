from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Redactor(AbstractUser):
    year_of_experience = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )

    REQUIRED_FIELDS = ["year_of_experience"]

    class Meta:
        verbose_name = "Redactor"
        verbose_name_plural = "Redactors"

    def get_absolute_url(self):
        return reverse("main:redactor-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


class Topic(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topics = models.ManyToManyField(Topic, related_name="newspapers")
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    class Meta:
        ordering = ["-published_date"]
        verbose_name = "Newspaper"
        verbose_name_plural = "Newspapers"

    def get_absolute_url(self):
        return reverse("main:newspaper-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.title} ({self.published_date:%Y-%m-%d})"


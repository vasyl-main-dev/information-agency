from django.contrib.auth.models import AbstractUser
from django.db import models


class Redactor(AbstractUser):
    year_of_experience = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    topics = models.ManyToManyField(Topic, related_name="newspapers")
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

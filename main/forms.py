from django.contrib.auth.forms import UserCreationForm
from django import forms

from main.models import Redactor, Newspaper, Topic


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "year_of_experience",
            "first_name",
            "last_name",
        )


class NewsCreationForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=Redactor.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
        label="Publishers",
    )

    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
        label="Topics",
    )

    class Meta:
        model = Newspaper
        fields = ("title", "content", "topics", "publishers")

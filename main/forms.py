from django.contrib.auth.forms import UserCreationForm
from django import forms

from main.models import Redactor, Newspaper, Topic


class RedactorCreationForm(UserCreationForm):
    year_of_experience = forms.IntegerField(
        min_value=0,
        max_value=50,
        label="Years of experience",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter years of experience"}),
    )

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


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "🔍 Search by title...",
                "class": "form-control"
            }
        ),
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "🔍 Search by username...",
                "class": "form-control"
            }
        )
    )

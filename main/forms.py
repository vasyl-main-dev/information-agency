from django.contrib.auth.forms import UserCreationForm

from main.models import Redactor


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "year_of_experience",
            "first_name",
            "last_name",
        )

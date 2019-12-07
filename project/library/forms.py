from django import forms

from library.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ["status"]


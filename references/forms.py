from django import forms
from . import models


class CreateGenre(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = {
            'genre',
            'description'
        }

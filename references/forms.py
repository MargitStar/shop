from django import forms
from . import models


class CreateGenre(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = (
            'genre',
            'description'
        )


class CreateAuthor(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = (
            'author',
            'biography'
        )


class CreateSeries(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = (
            'title',
            'description'
        )


class CreatePublishingHouse(forms.ModelForm):
    class Meta:
        model = models.PublishingHouse
        fields = (
            'house',
            'history'
        )


class UpdateGenre(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = (
            'genre',
            'description'
        )


class UpdateAuthor(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = (
            'author',
            'biography'
        )

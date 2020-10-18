from django.db import models


class Author(models.Model):
    author = models.CharField(
        "Author",
        max_length=30,
        blank=False,
        null=False
    )

    biography = models.TextField(
        "About author",
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.author


class Series(models.Model):
    title = models.CharField(
        "Title of series",
        max_length=100,
        blank=False,
        null=False
    )

    description = models.TextField(
        "About this series",
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre = models.CharField(
        "Genre",
        max_length=50,
        blank=False,
        null=False
    )

    description = models.TextField(
        "About this genre",
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.genre

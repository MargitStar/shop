from django.db import models
from references.models import *
from datetime import date


class Book(models.Model):
    name = models.CharField(
        "Title",
        max_length=100,
        blank=False,
        null=False
    )

    # cover_photo = models.CharField(
    #     "Cover"
    # )

    price = models.DecimalField(
        "Price in BYN",
        default=0.0,
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False
    )

    publishing_date = models.DateField(
        "Date of publishing",
        default=date.today,
        blank=False,
        null=False
    )

    pages_amount = models.IntegerField(
        "Amount of pages",
        default=0,
        blank=False,
        null=False
    )

    binding = models.CharField(
        "Binding",
        default="",
        max_length=50,
        blank=False,
        null=False
    )

    weight = models.IntegerField(
        "Weight (g)",
        default=0.0,
        blank=False,
        null=False
    )

    # genre = models.ManyToManyRel(Genre)

    def __str__(self):
        return self.name

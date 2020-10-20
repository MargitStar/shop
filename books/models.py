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

    pages_amount = models.PositiveIntegerField(
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

    weight = models.PositiveIntegerField(
        "Weight (g)",
        default=0.0,
        blank=False,
        null=False
    )

    AGE_LIMIT_CHOICES = (('1', '18+'), ('2', '16+'), ('3', '14+'),
                         ('4', '12+'), ('5', '10+'), ('6', '8+'),
                         ('7', '6+'), ('8', '3+'), ('6', '0+'))
    age_limit = models.CharField(
        "Age limit",
        max_length=4,
        default=1,
        choices=AGE_LIMIT_CHOICES,
        blank=False,
        null=False
    )

    CHOICES = (('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'),
               ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
               ('8', '8'), ('9', '9'), ('10', '10'))
    rating = models.CharField(
        "Rating",
        max_length=10,
        default=0,
        choices=CHOICES,
        blank=False,
        null=False
    )

    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    is_active = models.BooleanField(
        "Is active?",
        choices=BOOL_CHOICES,
        default=True,
        blank=False,
        null=False
    )

    # genre = models.ManyToManyRel(Genre)

    def __str__(self):
        return self.name

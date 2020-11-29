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

    cover_photo = models.ImageField(
        "Cover",
        default='',
        upload_to='media/'
    )

    author = models.ManyToManyField(
        Author
    )

    genre = models.ManyToManyField(
        Genre
    )

    series = models.ForeignKey(
        Series,
        default=1,
        on_delete=models.CASCADE
    )

    publishing_house = models.ForeignKey(
        PublishingHouse,
        default=1,
        on_delete=models.CASCADE
    )

    price = models.DecimalField(
        "Price in BYN",
        default=0.0,
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False
    )

    FORMAT_CHOICES = (('84×108/16', '84×108/16'), ('70×90/8', '70×90/8'), ('70×90/16', '70×90/16'),
                      ('75×90/16', '75×90/16'), ('60×90/16', '60×90/16'), ('84×108/32', '84×108/32'),
                      ('70×90/32', '70×90/32'), ('70×108/32', '70×108/32'), ('60×90/32', '60×90/32'))
    format = models.CharField(
        "Format",
        max_length=15,
        default=1,
        choices=FORMAT_CHOICES,
        blank=False,
        null=False
    )

    isbn_code = models.CharField(
        "ISBN",
        default='',
        max_length=20,
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
        default=0,
        blank=False,
        null=False
    )

    books_amount = models.PositiveIntegerField(
        "Left amount",
        default=0,
        blank=False,
        null=False
    )

    AGE_LIMIT_CHOICES = (('18+', '18+'), ('16+', '16+'), ('14+', '14+'),
                         ('12+', '12+'), ('10+', '10+'), ('8+', '8+'),
                         ('6+', '6+'), ('3+', '3+'), ('0+', '0+'))
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

    BOOL_CHOICES = (('Yes', 'Yes'), ('No', 'No'))
    is_active = models.CharField(
        "Is active?",
        choices=BOOL_CHOICES,
        max_length=3,
        default=True,
        blank=False,
        null=False
    )

    entry_date = models.DateTimeField(
        "Date of entry",
        auto_now_add=True,
        null=True,
        blank=True
    )

    update_date = models.DateTimeField(
        "Date of updating",
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

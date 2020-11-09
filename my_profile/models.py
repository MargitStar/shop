from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    username = models.CharField(
        'Username',
        max_length=50,
    )

    first_name = models.CharField(
        'First Name',
        max_length=50,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        'Last Name',
        max_length=50,
        blank=True,
        null=True
    )

    password = models.CharField(
        'Password',
        max_length=50
    )

    email = models.EmailField(
        'Email',
        max_length=50
    )

    phone_number = PhoneNumberField(
        'Phone Number',
        unique=True
    )

    country = CountryField(
        'Country',
        blank=True,
        null=True
    )

    city = models.CharField(
        'City',
        max_length=50,
        blank=True,
        null=True
    )

    zip_code = models.CharField(
        'Zip code',
        max_length=5,
        blank=True,
        null=True
    )

    address1 = models.CharField(
        'Address #1',
        max_length=50,
        blank=True,
        null=True
    )

    address2 = models.CharField(
        'Address #2',
        max_length=50,
        blank=True,
        null=True
    )

    additional_info = models.CharField(
        'Additional Information',
        max_length=200,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username

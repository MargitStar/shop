# Generated by Django 3.1.2 on 2020-11-09 20:49

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Last Name')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Phone Number')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Country')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('zip_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='Zip code')),
                ('address1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Address #1')),
                ('address2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Address #2')),
                ('additional_info', models.CharField(blank=True, max_length=200, null=True, verbose_name='Additional Information')),
            ],
        ),
    ]

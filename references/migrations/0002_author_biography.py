# Generated by Django 3.1.2 on 2020-10-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='About author'),
        ),
    ]

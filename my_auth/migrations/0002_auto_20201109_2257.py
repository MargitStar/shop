# Generated by Django 3.1.2 on 2020-11-09 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUser',
            new_name='User',
        ),
    ]

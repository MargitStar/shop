# Generated by Django 3.1.2 on 2020-12-01 21:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20201201_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='create',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 0, 0, 19, 893680)),
        ),
    ]

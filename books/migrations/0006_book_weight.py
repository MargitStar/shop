# Generated by Django 3.1.2 on 2020-10-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20201020_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='weight',
            field=models.IntegerField(default=0.0, verbose_name='Weight'),
        ),
    ]
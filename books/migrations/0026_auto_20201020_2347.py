# Generated by Django 3.1.2 on 2020-10-20 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0025_auto_20201020_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_photo',
            field=models.ImageField(upload_to='', verbose_name='Cover'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-20 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0022_book_isbn_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_photo',
            field=models.ImageField(default='/04blackhole1-articleLarge-v3.jpg', upload_to='static', verbose_name='Cover'),
        ),
    ]

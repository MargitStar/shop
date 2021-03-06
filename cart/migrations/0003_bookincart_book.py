# Generated by Django 3.1.2 on 2020-11-18 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20201110_2147'),
        ('cart', '0002_bookincart'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookincart',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='book_in_cart', to='books.book'),
        ),
    ]

from django.db import models

class Author(models.Model):
    author = models.CharField(
        "Author",
        max_length=30,
        blank=False,
        null=False
    )


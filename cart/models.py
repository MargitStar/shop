from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        related_name='templates',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    created_date = models.DateTimeField(
        "Created Date",
        auto_now_add=True,
        null=True,
        blank=True
    )

    updated_date = models.DateTimeField(
        "Updated Date",
        auto_now=True,
        null=True,
        blank=True
    )


class BookInCart(models.Model):
    cart = models.ForeignKey(
        "Cart",
        on_delete=models.CASCADE,
        related_name='books'
    )

    quantity = models.IntegerField(
        'Quantity',
        default=1
    )

    price = models.DecimalField(
        'Price',
        max_digits=10,
        decimal_places=2,
    )

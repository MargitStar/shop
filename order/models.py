from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cart.models import Cart


class Order(models.Model):
    cart = models.OneToOneField(
        Cart,
        on_delete=models.PROTECT,
    )

    status1 = models.BooleanField(
        'Cancel Order',
        default=False
    )

    status2 = models.CharField(
        'Status of order',
        choices=(
            ('The order is being processed', 'The order is being processed'),
            ('The order is being delivered', 'The order is being delivered'),
            ('The order was canceled', 'The order was canceled'),
            ('The order is completed', 'The order is completed')
        ),
        max_length=100,
    )

    delivery_address = models.CharField(
        'Delivery address',
        max_length=100
    )

    contact_phone = PhoneNumberField(
        'Phone number'
    )

    create_date = models.DateField(
        auto_now_add=True
    )

    update_date = models.DateField(
        auto_now=True
    )

    comment = models.TextField(
        'Comment',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Order #{self.pk}"

from django.shortcuts import render
from django.views.generic import TemplateView
from . import models


class CartView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        user = self.request.user
        if not isinstance(user, models.User):
            user = None

        cart, created = models.Cart.objects.get_or_create(
            pk=cart_id,
            defaults={
                'customer': user,
            }
        )

        context['cart'] = cart
        if created:
            self.request.session['cart_id'] = cart.pk

        return context

from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from . import models
from books import models as book_models


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


class AddBookToCart(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        user = self.request.user
        if not isinstance(user, models.User):
            user = None

        if cart_id:
            cart = models.Cart.objects.filter(pk=cart_id)
            if not cart:
                cart = models.Cart.objects.create(customer=user)
                self.request.session[cart_id] = cart.pk
        else:
            cart = models.Cart.objects.create(customer=user)
            self.request.session[cart_id] = cart.pk

        book_id = int(self.request.GET.get('book'))
        book = book_models.Book.objects.filter(pk=book_id).first()

        context['cart'] = cart
        context['book'] = book

        return context

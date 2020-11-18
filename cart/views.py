from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from . import models
from books import models as book_models


class CartView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        print(cart_id)
        user = self.request.user
        if not isinstance(user, models.User):
            user = None

        if cart_id:
            cart = models.Cart.objects.filter(pk=cart_id)
            if not cart:
                cart = models.Cart.objects.create(customer=user)
                self.request.session['cart_id'] = cart.pk
        else:
            cart = models.Cart.objects.create(customer=user)
            self.request.session['cart_id'] = cart.pk

        book = models.BookInCart.objects.all()

        context['cart'] = cart
        context['book'] = book
        return context


class AddBookToCart(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        print(cart_id)
        user = self.request.user
        if not isinstance(user, models.User):
            user = None

        if cart_id:
            cart = models.Cart.objects.filter(pk=cart_id).first()
            if not cart:
                cart = models.Cart.objects.create(customer=user)
                self.request.session['cart_id'] = cart.pk
        else:
            cart = models.Cart.objects.create(customer=user)
            self.request.session['cart_id'] = cart.pk
            print(self.request.session.items())

        book_id = int(self.request.GET.get('book'))
        book = book_models.Book.objects.filter(pk=book_id).first()

        if book:
            book_in_cart, created = models.BookInCart.objects.get_or_create(
                book=book,
                cart=cart,
                defaults={
                    'quantity': 1,
                    'price': book.price
                }
            )

            if not created:
                book_in_cart.quantity += 1
                book_in_cart.price = book_in_cart.book_total_price()
                book_in_cart.save()

        context['cart'] = cart
        context['book'] = book

        return context

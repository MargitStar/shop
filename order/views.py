from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Order
from my_profile.models import Profile
from cart.models import Cart, BookInCart
from books.models import Book


class CreateOrder(SuccessMessageMixin, UpdateView):
    template_name = 'order/create_order.html'
    model = Order
    fields = ('delivery_address', 'contact_phone', 'comment')
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_profile = Profile.objects.get(user=user)

        if user_profile.address1:
            delivery_address = user_profile.address1
        if user_profile.phone_number:
            contact_phone = user_profile.phone_number

        cart_id = self.request.session.get('cart_id')
        cart = Cart.objects.get(pk=cart_id)
        order_id = self.request.session.get('order_id')

        if order_id:
            order = Order.objects.filter(pk=order_id).first()
            if not order:
                order = Order.objects.create(cart=cart)
                self.request.session['order_id'] = order.pk
        else:
            order = Order.objects.create(cart=cart)
            self.request.session['order_id'] = order.pk

        context['order'] = order
        return context

    def get_success_url(self):
        cart_pk = self.request.session['cart_pk']
        del self.request.session['cart_pk']

        book_in_cart = BookInCart.objects.all().filter(cart=cart_pk)

        for book in book_in_cart:
            cur_book = Book.objects.filter(pk=book.books.pk).last()

            new_count = cur_book.books_amount - book.quantity
            if new_count >= 0:
                cur_book.books_amount = new_count
            else:
                book.quantity = cur_book.books_amount
                book.delete()
            cur_book.save()

            if cur_book.books_amount == 0:
                cur_book.is_active = False
                cur_book.save()

        order_id = self.object.pk
        order = Order.objects.filter(pk=order_id).first()
        order.user = self.request.user

        return reverse_lazy('profile:profile_view')

    def get_success_message(self, cleaned_data):
        message = messages.success(
            f"Your order {self.object} was created successfully. We will call you to confirm the order soon!"
        )
        return message

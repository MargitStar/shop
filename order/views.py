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


class CreateOrder(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'order/create_order.html'
    model = Order
    fields = ('delivery_address', 'contact_phone', 'comment')
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        user = self.request.user
        user_profile = Profile.objects.get(user=user)

        cart_id = self.request.session.get('cart_id')
        cart = Cart.objects.get(pk=cart_id)
        order_id = self.request.session.get('order_id')

        book_in_cart = BookInCart.objects.all().filter(cart_id=cart_id)

        for book in book_in_cart:
            cur_book = Book.objects.filter(pk=book.book.pk).last()

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

        book_in_cart_new = BookInCart.objects.all().filter(cart=cart_id)
        if len(book_in_cart_new) == 0:
            return None

        order = Order.objects.create(cart=cart)
        self.request.session['order_id'] = order.pk

        if user_profile.address1:
            order.delivery_address = user_profile.address1
        if user_profile.phone_number:
            order.contact_phone = user_profile.phone_number
            order.save()
        del self.request.session['cart_id']
        return order

    def get_success_url(self):
        del self.request.session['order_id']
        return reverse_lazy('profile:profile_view')

    def get_success_message(self, cleaned_data):
        message = messages.success(
            f"Your order {self.object} was created successfully. We will call you to confirm the order soon!"
        )
        return message


class CancelOrder(LoginRequiredMixin, UpdateView):
    template_name = 'order/update_order.html'
    model = Order
    fields = ('status1',)
    success_url = reverse_lazy('profile:profile_view')
    login_url = reverse_lazy('login')

    def get_success_url(self):
        order_id = self.request.session.get('order_id')
        order = Order.objects.get(id=order_id)
        if order.status1:
            new_order = Order.objects.filter(pk=order_id).first()
            new_order.status2 = 'The order was canceled'
            new_order.save()
            return reverse_lazy('profile:profile_view')
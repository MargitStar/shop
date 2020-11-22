from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from my_profile.models import Profile
from cart.models import Cart


class CreateOrder(CreateView):
    template_name = 'order/create_order.html'
    model = Order
    fields = ('delivery_address', 'contact_phone', 'comment')
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_profile = Profile.objects.get(user=user)

        delivery_address = user_profile.address1
        phone_number = user_profile.phone_number

        cart_id = self.request.session.get('cart_id')
        cart = Cart.objects.get(pk=cart_id)
        order_id = self.request.session.get('order_id')

        if order_id:
            order = Order.objects.filter(pk=order_id).first()
            if not order:
                order = Order.objects.create(cart=cart, delivery_address=delivery_address, contact_phone=phone_number)
                self.request.session['order_id'] = order.pk
        else:
            order = Order.objects.create(cart=cart, delivery_address=delivery_address, contact_phone=phone_number)
            self.request.session['order_id'] = order.pk

        context['order'] = order

        return context

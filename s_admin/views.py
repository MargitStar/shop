from django.shortcuts import render

from cart.models import BookInCart, Cart

from books.models import Book

from order.models import Order

from references import models as ref_models

from my_profile.models import Profile
from my_profile import views as my_profile_views

from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class SAdminOrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 's_admin/order/s_admin_order_list.html'
    success_url = reverse_lazy('s_admin:s_admin_order_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminOrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 's_admin/order/s_admin_order_update.html'
    fields = ('status2', 'delivery_address', 'contact_phone', 'comment')
    success_url = reverse_lazy('s_admin:s_admin_order_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminOrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 's_admin/order/s_admin_order_delete.html'
    success_url = reverse_lazy('s_admin:s_admin_order_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminGenreList(LoginRequiredMixin, ListView):
    model = ref_models.Genre
    template_name = 's_admin/genre/s_admin_genre_list.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminGenreCreate(LoginRequiredMixin, CreateView):
    model = ref_models.Genre
    fields = '__all__'
    success_url = reverse_lazy('s_admin:s_admin_genre_list')
    template_name = 's_admin/genre/s_admin_genre_create.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminGenreUpdate(LoginRequiredMixin, UpdateView):
    model = ref_models.Genre
    fields = '__all__'
    success_url = reverse_lazy('s_admin:s_admin_genre_list')
    template_name = 's_admin/genre/s_admin_genre_update.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminGenreDelete(LoginRequiredMixin, DeleteView):
    model = ref_models.Genre
    success_url = reverse_lazy('s_admin:s_admin_genre_list')
    template_name = 's_admin/genre/s_admin_genre_delete.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminGenreView(LoginRequiredMixin, DetailView):
    model = ref_models.Genre
    template_name = 's_admin/genre/s_admin_genre_view.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

from django.shortcuts import render

from cart.models import BookInCart, Cart

from books.models import Book
from books import views as book_view

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
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminOrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 's_admin/order/s_admin_order_update.html'
    fields = ('status2', 'delivery_address', 'contact_phone', 'comment')
    success_url = reverse_lazy('s_admin:s_admin_order_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminOrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 's_admin/order/s_admin_order_delete.html'
    success_url = reverse_lazy('s_admin:s_admin_order_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminGenreList(LoginRequiredMixin, ListView):
    model = ref_models.Genre
    template_name = 's_admin/genre/s_admin_genre_list.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminGenreCreate(LoginRequiredMixin, CreateView):
    model = ref_models.Genre
    fields = '__all__'
    success_url = reverse_lazy('s_admin:s_admin_genre_list')
    template_name = 's_admin/genre/s_admin_genre_create.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminGenreUpdate(LoginRequiredMixin, UpdateView):
    model = ref_models.Genre
    fields = '__all__'
    success_url = reverse_lazy('s_admin:s_admin_genre_list')
    template_name = 's_admin/genre/s_admin_genre_update.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminGenreDelete(LoginRequiredMixin, DeleteView):
    model = ref_models.Genre
    success_url = reverse_lazy('s_admin:s_admin_genre_list')
    template_name = 's_admin/genre/s_admin_genre_delete.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminGenreView(LoginRequiredMixin, DetailView):
    model = ref_models.Genre
    template_name = 's_admin/genre/s_admin_genre_view.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminSeriesList(LoginRequiredMixin, ListView):
    model = ref_models.Series
    template_name = 's_admin/series/s_admin_series_list_view.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminSeriesUpdate(LoginRequiredMixin, UpdateView):
    model = ref_models.Series
    fields = '__all__'
    success_url = reverse_lazy('s_admin:s_admin_series_list')
    template_name = 's_admin/series/s_admin_series_update.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminSeriesDelete(LoginRequiredMixin, DeleteView):
    model = ref_models.Series
    success_url = reverse_lazy('s_admin:s_admin_series_list')
    template_name = 's_admin/series/s_admin_series_delete.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminSeriesCreate(LoginRequiredMixin, CreateView):
    model = ref_models.Series
    fields = '__all__'
    success_url = reverse_lazy('s_admin:s_admin_series_list')
    template_name = 's_admin/series/s_admin_series_create.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminSeriesView(LoginRequiredMixin, DetailView):
    model = ref_models.Series
    template_name = 's_admin/series/s_admin_series_view.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminAuthorList(LoginRequiredMixin, ListView):
    model = ref_models.Author
    template_name = 's_admin/author/s_admin_author_list.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminAuthorDelete(LoginRequiredMixin, DeleteView):
    model = ref_models.Author
    success_url = reverse_lazy('s_admin:s_admin_author_list')
    template_name = 's_admin/author/s_admin_author_delete.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminAuthorUpdate(LoginRequiredMixin, UpdateView):
    model = ref_models.Author
    fields = '__all__'
    success_url = reverse_lazy('s_admin:s_admin_author_list')
    template_name = 's_admin/series/s_admin_series_update.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminAuthorCreate(LoginRequiredMixin, CreateView):
    model = ref_models.Author
    fields = '__all__'
    success_url = reverse_lazy('s_admin:s_admin_author_list')
    template_name = 's_admin/author/s_admin_author_create.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminAuthorView(LoginRequiredMixin, DetailView):
    model = ref_models.Author
    template_name = 's_admin/author/s_admin_author_view.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminPublishingHouseList(LoginRequiredMixin, ListView):
    model = ref_models.PublishingHouse
    template_name = 's_admin/publishing_house/s_admin_publishing_house_list.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminPublishingHouseView(LoginRequiredMixin, DetailView):
    model = ref_models.PublishingHouse
    template_name = 's_admin/publishing_house/s_admin_publishing_house_view.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminPublishingHouseCreate(LoginRequiredMixin, CreateView):
    model = ref_models.PublishingHouse
    fields = '__all__'
    success_url = reverse_lazy('s_admin:s_admin_publishing_house_list')
    template_name = 's_admin/publishing_house/s_admin_publishing_house_create.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminPublishingHouseUpdate(LoginRequiredMixin, UpdateView):
    model = ref_models.PublishingHouse
    fields = '__all__'
    success_url = reverse_lazy('s_admin:s_admin_publishing_house_list')
    template_name = 's_admin/publishing_house/s_admin_publishing_house_update.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminPublishingHouseDelete(LoginRequiredMixin, DeleteView):
    model = ref_models.PublishingHouse
    success_url = reverse_lazy('s_admin:s_admin_publishing_house_list')
    template_name = 's_admin/publishing_house/s_admin_publishing_house_delete.html'

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminBookList(LoginRequiredMixin, book_view.BookListView):
    template_name = 's_admin/book/s_admin_book_list.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminBookDelete(LoginRequiredMixin, book_view.DeleteBookView):
    template_name = 's_admin/book/s_admin_book_delete.html'
    success_url = reverse_lazy('s_admin:s_admin_book_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminBookUpdate(LoginRequiredMixin, book_view.UpdateBook):
    template_name = 's_admin/book/s_admin_book_update.html'
    success_url = reverse_lazy('s_admin:s_admin_book_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminBookCreate(book_view.CreateBook):
    template_name = 's_admin/book/s_admin_book_create.html'
    success_url = reverse_lazy('s_admin:s_admin_book_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class SAdminBookView(LoginRequiredMixin, book_view.BookView):
    template_name = 's_admin/book/s_admin_book_view.html'
    success_url = reverse_lazy('s_admin:s_admin_book_list')

    def get_queryset(self):
        if self.request.user.groups.filter(name='Customer'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class CustomersList(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 's_admin/customer/s_admin_customer_list.html'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class CustomerUpdate(my_profile_views.UpdateProfileView):
    template_name = 's_admin/customer/s_admin_customer_update.html'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()


class CustomerView(my_profile_views.ProfileView):
    template_name = 's_admin/customer/s_admin_customer_view.html'

    def get_queryset(self, *args, **kwargs):
        if self.request.user.groups.filter(name='Customers'):
            return self.handle_no_permission()
        else:
            return self.model.objects.all()

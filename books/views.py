from django.shortcuts import render
from books import forms, models
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(ListView):
    template_name = 'books/book_list.html'
    model = models.Book


class BookView(DetailView):
    template_name = 'books/book_view.html'
    model = models.Book


class CreateBook(LoginRequiredMixin, CreateView):
    template_name = 'books/create_book.html'
    model = models.Book
    form_class = forms.CreateBook
    success_url = '/book'
    login_url = '/login'


class UpdateBook(UpdateView):
    template_name = 'books/update_book.html'
    model = models.Book
    form_class = forms.UpdateBook
    success_url = '/book'


class DeleteBookView(DeleteView):
    model = models.Book
    template_name = 'refs/delete_view.html'
    success_url = '/book'

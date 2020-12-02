from django.shortcuts import render

from books import models
from django.views.generic import TemplateView


class TopBooksListView(TemplateView):
    template_name = 'home_screen/top_books_list_view.html'
    model = models.Book

    def get_context_data(self, **kwargs):
        filtered = models.Book.objects.order_by('-entry_date')
        most_popular = models.Book.objects.order_by('-price')
        return {'books': filtered[0:10], 'most_popular': most_popular[::-1][0:10]}

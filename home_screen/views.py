from django.shortcuts import render

from books import models
from django.views.generic import TemplateView
import requests


class TopBooksListView(TemplateView):
    template_name = 'home_screen/top_books_list_view.html'
    model = models.Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filtered = models.Book.objects.order_by('-entry_date')
        most_popular = models.Book.objects.order_by('-price')
        rating = models.Book.objects.order_by('-rating')
        s = requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0')
        result = s.json()
        rate = {}
        for d in result:
            if d.get('Cur_Abbreviation') == 'USD':
                rate['USD'] = d.get('Cur_OfficialRate') * d.get('Cur_Scale')
            elif d.get('Cur_Abbreviation') == 'EUR':
                rate['EUR'] = d.get('Cur_OfficialRate') * d.get('Cur_Scale')
            elif d.get('Cur_Abbreviation') == 'RUB':
                rate['RUB'] = d.get('Cur_OfficialRate') * d.get('Cur_Scale')
        return {'books': filtered[0:10], 'most_popular': most_popular[::-1][0:10], 'rating': rating[0:10],
                'USD': rate.get('USD'), 'EUR': rate.get('EUR'), 'RUB': rate.get('RUB'), 'rate': rate}

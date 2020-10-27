from django.shortcuts import render
from references import models


# Create your views here.

def genre_list_view(request):
    context = {'genres': models.Genre.objects.all()}
    return render(request, template_name='refs/list_view.html', context=context)


def genre_view(request, pk_obj):
    context = {'genre': models.Genre.objects.get(pk=pk_obj)}
    return render(request, template_name='refs/genre_view.html', context=context)

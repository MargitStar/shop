from django.shortcuts import render
from references import models
from references import forms
from django.http import HttpResponseRedirect


# Create your views here.

def genre_list_view(request):
    context = {'genres': models.Genre.objects.all()}
    return render(request, template_name='refs/genre_list_view.html', context=context)


def genre_view(request, pk_obj):
    context = {'genre': models.Genre.objects.get(pk=pk_obj)}
    return render(request, template_name='refs/genre_view.html', context=context)


def author_list_view(request):
    context = {'authors': models.Author.objects.all()}
    return render(request, template_name='refs/author_list_view.html', context=context)


def author_view(request, pk_obj):
    context = {'author': models.Author.objects.get(pk=pk_obj)}
    return render(request, template_name='refs/author_view.html', context=context)


def publishing_house_list_view(request):
    context = {'publishing_houses': models.PublishingHouse.objects.all()}
    return render(request, template_name='refs/publishing_house_list_view.html', context=context)


def publishing_house_view(request, pk_obj):
    context = {'publishing_house': models.PublishingHouse.objects.get(pk=pk_obj)}
    return render(request, template_name='refs/publishing_house_view.html', context=context)


def series_list_view(request):
    context = {'series_list': models.Series.objects.all()}
    return render(request, template_name='refs/series_list_view.html', context=context)


def series_view(request, pk_obj):
    context = {'series': models.Series.objects.get(pk=pk_obj)}
    return render(request, template_name='refs/series_view.html', context=context)


def create_genre(request):
    if request.method == "POST":
        form = forms.CreateGenre(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/genre')
    else:
        form = forms.CreateGenre()

    return render(request, template_name='refs/create_genre.html', context={'form': form})

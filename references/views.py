from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from references import models
from references import forms


class GenreListView(ListView):
    template_name = 'refs/genre_list_view.html'
    model = models.Genre


class AuthorListView(ListView):
    template_name = 'refs/author_list_view.html'
    model = models.Author


class PublishingHouseListView(ListView):
    template_name = 'refs/publishing_house_list_view.html'
    model = models.PublishingHouse


class SeriesListView(ListView):
    template_name = 'refs/series_list_view.html'
    model = models.Series


class GenreView(DetailView):
    template_name = 'refs/genre_view.html'
    model = models.Genre


class AuthorView(DetailView):
    template_name = 'refs/author_view.html'
    model = models.Author


# TODO: some fucking shit happens, don't know why FIX
class PublishingHouseView(DetailView):
    template_name = 'refs/publishing_house_view.html'
    model = models.PublishingHouse


class SeriesView(DetailView):
    template_name = 'refs/series_view.html'
    model = models.Series


class CreateGenre(CreateView):
    template_name = 'refs/create_genre.html'
    model = models.Genre
    form_class = forms.CreateGenre
    success_url = '/genre'


class CreateAuthor(CreateView):
    template_name = 'refs/create_author.html'
    model = models.Author
    form_class = forms.CreateAuthor
    success_url = '/author'


class CreatePublishingHouse(CreateView):
    template_name = 'refs/create_publishing_house.html'
    model = models.PublishingHouse
    form_class = forms.CreatePublishingHouse
    success_url = '/publishing_house'


class CreateSeries(CreateView):
    template_name = 'refs/create_series.html'
    model = models.Series
    form_class = forms.CreateSeries
    success_url = '/series'


class UpdateGenre(UpdateView):
    template_name = 'refs/update_genre.html'
    model = models.Genre
    form_class = forms.UpdateGenre
    success_url = '/genre'


class UpdateAuthor(UpdateView):
    template_name = 'refs/update_author.html'
    model = models.Author
    form_class = forms.UpdateAuthor
    success_url = '/author'


class UpdatePublishingHouse(UpdateView):
    template_name = 'refs/update_publishing_house.html'
    model = models.PublishingHouse
    form_class = forms.UpdatePublishingHouse
    success_url = '/publishing_house'


class UpdateSeries(UpdateView):
    template_name = 'refs/update_series.html'
    model = models.Series
    form_class = forms.UpdateSeries
    success_url = '/series'


def update_author(request, pk_obj):
    if request.method == "POST":
        form = forms.UpdateAuthor(data=request.POST)
        if form.is_valid():
            author = form.cleaned_data.get('author')
            biography = form.cleaned_data.get('biography')
            new_author = models.Author.objects.get(pk=pk_obj)
            new_author.author = author
            new_author.biography = biography
            new_author.save()
            return HttpResponseRedirect(f'/author/{pk_obj}')
    else:
        author = models.Author.objects.get(pk=pk_obj)
        form = forms.UpdateAuthor(data={'author': author.author, 'biography': author.biography})
        return render(request, template_name='refs/update_author.html', context={'form': form})


def update_series(request, pk_obj):
    if request.method == "POST":
        form = forms.UpdateSeries(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            new_title = models.Series.objects.get(pk=pk_obj)
            new_title.title = title
            new_title.description = description
            new_title.save()
            return HttpResponseRedirect(f'/series/{pk_obj}')
    else:
        title = models.Series.objects.get(pk=pk_obj)
        form = forms.UpdateSeries(data={'title': title.title, 'description': title.description})
        return render(request, template_name='refs/update_series.html', context={'form': form})


def update_publishing_house(request, pk_obj):
    if request.method == "POST":
        form = forms.UpdatePublishingHouse(data=request.POST)
        if form.is_valid():
            house = form.cleaned_data.get('house')
            history = form.cleaned_data.get('history')
            new_house = models.PublishingHouse.objects.get(pk=pk_obj)
            new_house.house = house
            new_house.history = history
            new_house.save()
            return HttpResponseRedirect(f'/publishing_house/{pk_obj}')
    else:
        house = models.PublishingHouse.objects.get(pk=pk_obj)
        form = forms.UpdatePublishingHouse(data={'house': house.house, 'history': house.history})
        return render(request, template_name='refs/update_publishing_house.html', context={'form': form})


class DeleteGenreView(DeleteView):
    model = models.Genre
    template_name = 'refs/delete_view.html'
    success_url = '/genre'


class DeleteAuthorView(DeleteView):
    model = models.Author
    template_name = 'refs/delete_view.html'
    success_url = '/author'


class DeletePublishingHouseView(DeleteView):
    model = models.PublishingHouse
    template_name = 'refs/delete_view.html'
    success_url = '/publishing_house'


class DeleteSeriesView(DeleteView):
    model = models.Series
    template_name = 'refs/delete_view.html'
    success_url = '/series'

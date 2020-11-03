from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView

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


def genre_view(request, pk_obj):
    context = {'genre': models.Genre.objects.get(pk=pk_obj)}
    return render(request, template_name='refs/genre_view.html', context=context)




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


def create_author(request):
    if request.method == "POST":
        form = forms.CreateAuthor(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/author')
    else:
        form = forms.CreateAuthor()

    return render(request, template_name='refs/create_author.html', context={'form': form})


def create_series(request):
    if request.method == "POST":
        form = forms.CreateSeries(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/series')
    else:
        form = forms.CreateSeries()

    return render(request, template_name='refs/create_series.html', context={'form': form})


def create_publishing_house(request):
    if request.method == "POST":
        form = forms.CreatePublishingHouse(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/publishing_house')
    else:
        form = forms.CreatePublishingHouse()

    return render(request, template_name='refs/create_publishing_house.html', context={'form': form})


def update_genre(request, pk_obj):
    if request.method == "POST":
        form = forms.UpdateGenre(data=request.POST)
        if form.is_valid():
            genre = form.cleaned_data.get('genre')
            description = form.cleaned_data.get('description')
            new_genre = models.Genre.objects.get(pk=pk_obj)
            new_genre.genre = genre
            new_genre.description = description
            new_genre.save()
            return HttpResponseRedirect(f'/genre/{pk_obj}')
    else:
        genre = models.Genre.objects.get(pk=pk_obj)
        form = forms.UpdateGenre(data={'genre': genre.genre, 'description': genre.description})
        return render(request, template_name='refs/update_genre.html', context={'form': form})


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


def delete_genre(request, pk_obj):
    if request.method == "POST":
        genre = models.Genre.objects.get(pk=pk_obj)
        genre.delete()
        return HttpResponseRedirect('/genre')
    else:
        genre = models.Genre.objects.get(pk=pk_obj)
    return render(request, template_name='refs/delete_view.html', context={'genre': genre, 'header': genre.genre})


def delete_author(request, pk_obj):
    if request.method == "POST":
        author = models.Author.objects.get(pk=pk_obj)
        author.delete()
        return HttpResponseRedirect('/author')
    else:
        author = models.Author.objects.get(pk=pk_obj)
    return render(request, template_name='refs/delete_view.html', context={'author': author, 'header': author.author})


def delete_series(request, pk_obj):
    if request.method == "POST":
        series = models.Series.objects.get(pk=pk_obj)
        series.delete()
        return HttpResponseRedirect('/series')
    else:
        series = models.Series.objects.get(pk=pk_obj)
    return render(request, template_name='refs/delete_view.html', context={'series': series, 'header': series.title})


def delete_publishing_house(request, pk_obj):
    if request.method == "POST":
        house = models.PublishingHouse.objects.get(pk=pk_obj)
        house.delete()
        return HttpResponseRedirect('/publishing_house')
    else:
        house = models.PublishingHouse.objects.get(pk=pk_obj)
    return render(request, template_name='refs/delete_view.html', context={'house': house, 'header': house.house})

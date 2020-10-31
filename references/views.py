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
            return HttpResponseRedirect('/genre')
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
            return HttpResponseRedirect('/author')
    else:
        author = models.Author.objects.get(pk=pk_obj)
        form = forms.UpdateAuthor(data={'author': author.author, 'biography': author.biography})
        return render(request, template_name='refs/update_author.html', context={'form': form})

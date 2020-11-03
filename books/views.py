from django.shortcuts import render
from books import forms, models
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView


class BookListView(ListView):
    template_name = 'books/book_list.html'
    model = models.Book


class BookView(DetailView):
    template_name = 'books/book_view.html'
    model = models.Book


def book_list_view(request):
    context = {'books': models.Book.objects.all()}
    return render(request, template_name='books/book_list.html', context=context)


def book_view(request, pk_obj):
    book = models.Book.objects.get(pk=pk_obj)
    context = {'book': book}
    return render(request, template_name='books/book_view.html', context=context)


def create_book(request):
    if request.method == 'POST':
        form = forms.CreateBook(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book')
    else:
        form = forms.CreateBook()

    return render(request, template_name='books/create_book.html', context={'form': form})


def update_book(request, pk_obj):
    if request.method == "POST":
        form = forms.UpdateBook(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            cover_photo = form.cleaned_data.get('cover_photo')
            author = form.cleaned_data.get('author')
            genre = form.cleaned_data.get('genre')
            series = form.cleaned_data.get('series')
            publishing_house = form.cleaned_data.get('publishing_house')
            price = form.cleaned_data.get('price')
            book_format = form.cleaned_data.get('format')
            isbn_code = form.cleaned_data.get('isbn_code')
            publishing_date = form.cleaned_data.get('publishing_date')
            pages_amount = form.cleaned_data.get('pages_amount')
            binding = form.cleaned_data.get('binding')
            weight = form.cleaned_data.get('weight')
            books_amount = form.cleaned_data.get('books_amount')
            age_limit = form.cleaned_data.get('age_limit')
            rating = form.cleaned_data.get('rating')
            is_active = form.cleaned_data.get('is_active')

            new_book = models.Book.objects.get(pk=pk_obj)
            new_book.name = name
            new_book.cover_photo = cover_photo
            new_book.author.set(author)
            new_book.genre.set(genre)
            new_book.series = series
            new_book.publishing_house = publishing_house
            new_book.price = price
            new_book.format = book_format
            new_book.isbn_code = isbn_code
            new_book.publishing_date = publishing_date
            new_book.pages_amount = pages_amount
            new_book.binding = binding
            new_book.weight = weight
            new_book.books_amount = books_amount
            new_book.age_limit = age_limit
            new_book.rating = rating
            new_book.is_active = is_active

            new_book.save()
            return HttpResponseRedirect(f'/book/{pk_obj}')
    else:
        book = models.Book.objects.get(pk=pk_obj)
        form = forms.UpdateBook(instance=book)
    return render(request, template_name='books/update_book.html', context={'form': form})


def delete_book(request, pk_obj):
    if request.method == "POST":
        book = models.Book.objects.get(pk=pk_obj)
        book.delete()
        return HttpResponseRedirect('/book')
    else:
        book = models.Book.objects.get(pk=pk_obj)
    return render(request, template_name='refs/delete_view.html', context={'book': book, 'header': book.name})

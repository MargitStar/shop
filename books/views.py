from django.shortcuts import render
from books import forms, models
from django.http import HttpResponseRedirect


def book_list_view(request):
    context = {'books': models.Book.objects.all()}
    return render(request, template_name='books/book_list.html', context=context)


def book_view(request, pk_obj):
    book = models.Book.objects.get(pk=pk_obj)
    form = forms.BookForm(data={'name': book.name,
                                'author': book.author,
                                'genre': book.genre,
                                'series': book.series,
                                'publishing_house': book.publishing_house,
                                'price': book.price,
                                'format': book.format,
                                'isbn_code': book.isbn_code,
                                'publishing_date': book.publishing_date,
                                'pages_amount': book.pages_amount,
                                'binding': book.binding,
                                'weight': book.weight,
                                'books_amount': book.books_amount,
                                'age_limit': book.age_limit,
                                'rating': book.rating,
                                'is_active': book.is_active
                                })
    return render(request, template_name='books/book_view.html', context={'form': form})


def create_book(request):
    if request.method == 'POST':
        form = forms.CreateBook(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book')
    else:
        form = forms.CreateBook()

    return render(request, template_name='books/create_book.html', context={'form': form})


def delete_book(request, pk_obj):
    if request.method == "POST":
        book = models.Book.objects.get(pk=pk_obj)
        book.delete()
        return HttpResponseRedirect('/book')
    else:
        book = models.Book.objects.get(pk=pk_obj)
    return render(request, template_name='refs/delete_view.html', context={'book': book, 'header': book.name})

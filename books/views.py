from django.shortcuts import render
from books import forms, models
from django.http import HttpResponseRedirect


def book_list_view(request):
    context = {'books': models.Book.objects.all()}
    return render(request, template_name='books/book_list.html', context=context)


def book_view(request, pk_obj):
    book = models.Book.objects.get(pk=pk_obj)
    context = {'book': book}
    return render(request, template_name='books/book_view.html', context=context)


def create_book(request):
    if request.method == 'POST':
        form = forms.CreateBook(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book')
    else:
        form = forms.CreateBook()

    return render(request, template_name='books/create_book.html', context={'form': form})


def update_book(request, pk_obj):
    if request.method == "POST":
        form = forms.UpdateBook(data=request.POST)
        if form.is_valid():
            book = models.Book.objects.get(pk=pk_obj)
            updated_book = forms.UpdateBook()


def delete_book(request, pk_obj):
    if request.method == "POST":
        book = models.Book.objects.get(pk=pk_obj)
        book.delete()
        return HttpResponseRedirect('/book')
    else:
        book = models.Book.objects.get(pk=pk_obj)
    return render(request, template_name='refs/delete_view.html', context={'book': book, 'header': book.name})

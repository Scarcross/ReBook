# Create your views here.
from django.shortcuts import render_to_response ,render
from bookshop.models import Book


def index(request):
    return render_to_response('bookshop/index.html')


def booklist(request):
    booklist = Book.objects.all();
    for book in booklist:
        if len(str(book.description)) > 20:
            book.description = book.description[:150]+'...'
        print(book.title)
    if booklist is None:
        booklist = 'keine Eintraege vorhanden'
    return render(request, 'bookshop/booklist.html', {'books': booklist})

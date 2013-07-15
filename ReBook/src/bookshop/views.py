# Create your views here.
from django.shortcuts import render_to_response
from bookshop.models import Book


def index(request):
    return render_to_response('bookshop/index.html')


def booklist(request):
    booklist = Book.objects.all();
    for book in booklist:
        print(book.title)
    if booklist is None:
        booklist = 'keine Eintraege vorhanden'
    return render_to_response('bookshop/booklist.html', {'booklist', 'sdaosidassa'})

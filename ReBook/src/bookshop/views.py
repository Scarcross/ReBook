# Create your views here.
from django.shortcuts import render_to_response ,render
from bookshop.models import Book
from django.template.context import Context

def index(request):
    link = [{'name':'bookshop/booklist.html'},
            {'name':'index.html'}]
    c = Context({'toplevellinks': link})
    return render(request,'bookshop/index.html',c)


def booklist(request):
    booklist = Book.objects.all();
    for book in booklist:
        if len(str(book.description)) > 150:
            book.description = book.description[:150]+'...'
        
    if booklist is None:
        booklist = 'keine Eintraege vorhanden'
    return render(request, 'bookshop/booklist.html',{'books':booklist})

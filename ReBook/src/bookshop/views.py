# Create your views here.
from django.shortcuts import render
from bookshop.models import Book
from django.core.context_processors import csrf


def index(request):
    args = {}
    args.update(csrf(request))
 
    return render(request,'bookshop/index.html',args)


def booklist(request):
    
    args = {}
    args.update(csrf(request))
    booklist = Book.objects.all();
   
    for book in booklist:
        if len(str(book.description)) > 150:
            book.description = book.description[:150]+'...'
        
    if booklist is None:
        booklist = 'keine Eintraege vorhanden'
    
    args['books'] = booklist
    return render(request, 'bookshop/booklist.html',args)

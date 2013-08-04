# Create your views here.
from bookshop.models import Book, Genre
from django.core.context_processors import csrf
from django.shortcuts import render


def index(request):
    args = {}
    args.update(csrf(request))
    args['recentbooks'] = Book.objects.all().order_by('date_added')
    return render(request,'bookshop/index.html',args)

def booklist(request,bookid=None):
    args = {}
    args.update(csrf(request))
    booklist = None
    if bookid is None:
        booklist = Book.objects.all();
        for book in booklist:
            if len(str(book.description)) > 150:
                book.description = book.description[:150]+'...'
    else:
        booklist = [Book.objects.all().get(id=bookid)]

        if len(str(booklist[0].description)) > 150:
                booklist[0].description = booklist[0].description[:150]+'...'
        
    if booklist is None:
        booklist = 'keine Eintraege vorhanden'
    
    args['booklist'] = booklist
    return render(request, 'bookshop/booklist.html',args)


def genre(request,genreid=None):
    args ={}
#Print all Genres on right side
    genres = Genre.objects.all()
#get human readable bnames
    dictgen = dict()
    for gen in genres:
        dictgen[gen.id] = gen.get_genrename_display()
    args['genres']=dictgen
# Print selected genre
    if genreid is not None:
        genrename = Genre.objects.get(id = genreid)
        filteredbooks = Book.objects.all().filter(genre__genrename__exact=genrename)
        args['foundgenres']=filteredbooks
        
    return render(request,'bookshop/genre.html',args)


def selldialog(request):
    return render(request,'bookshop/sellDialog.html')
    



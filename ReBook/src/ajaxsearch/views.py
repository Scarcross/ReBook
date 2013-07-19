from bookshop import models
from django.template.defaultfilters import title
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def search_titles(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    
    else: 
        search_text = ''
   
    args = {}
    args.update(csrf(request))
    args['books'] = models.Book.objects.filter(title__contains=search_text) 
    
    for book in args.get('books'):
        print(book.title)
    
    return render_to_response('ajax/ajax_search.html', args)
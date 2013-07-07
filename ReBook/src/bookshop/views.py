# Create your views here.
from django.views import generic
from bookshop.models import Book


class IndexView(generic.ListView):
    template_name = 'bookshop/index.html'
    context_object_name = 'booklist'
    
    def queryset(self):
        return Book.objects.all()

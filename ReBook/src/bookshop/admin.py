'''
Created on 07.07.2013

@author: richman
'''
from django.contrib import admin
from bookshop.models import Book,Author,Publisher

class BookAdmin(admin.ModelAdmin):
    admin.site.register(Book)    
    admin.site.register(Author)
    admin.site.register(Publisher)
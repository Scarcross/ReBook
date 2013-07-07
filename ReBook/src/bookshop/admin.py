'''
Created on 07.07.2013

@author: richman
'''
from django.contrib import admin
from bookshop.models import Book,LastOwner


class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book)
        
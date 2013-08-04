'''
Created on 07.07.2013

@author: richman
'''
from django.conf.urls import patterns, include, url
from bookshop import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index' ),
    url(r'^booklist/$', views.booklist, name='booklist'),
    url(r'^booklist/(?P<bookid>\d+)/$', views.booklist, name='booklist'),
    url(r'^genre/$', views.genre, name='genre'),
    url(r'^genre/(?P<genreid>\w+)/$', views.genre, name='genre'),
    url(r'^sell/$',views.selldialog,name='sell'),
    
)
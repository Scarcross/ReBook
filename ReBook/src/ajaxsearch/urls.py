'''
Created on 17.07.2013

@author: leip
'''
from django.conf.urls import patterns,  url
from ajaxsearch import views

urlpatterns = patterns('',
  
    url(r'^$',views.search_titles),
)
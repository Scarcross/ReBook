'''
Created on 16.07.2013

@author: leip
'''

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',  
    url(r'^newsletter_add/$', newsletter_add, name="newsletter_add"),  
)  
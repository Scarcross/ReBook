'''
Created on 07.07.2013

@author: richman
'''
from django.conf.urls import patterns, include, url
from bookshop import views

urlpatterns = patterns('',
                           
url(r'^$', views.IndexView.as_view(), name='index'),

)
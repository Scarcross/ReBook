'''
Created on 09.07.2013

@author: leip
'''
from django.conf.urls import patterns, include, url
from userauth import views

urlpatterns = patterns('',
                           
    url(r'^$', views.login, name='login'),
    url(r'^/login/$', views.login, name='login'),
    url(r'^/logout/$', views.login, name='login'),

)
'''
Created on 09.07.2013

@author: leip
'''
from django.conf.urls import patterns, include, url
from userauth import views

urlpatterns = patterns('',
                           
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^thanks/',views.thanks,name='thanks'),
)
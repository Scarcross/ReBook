'''
Created on 09.07.2013

@author: leip
'''
from django.conf.urls import patterns,  url
from userauth import views
from django.contrib.auth.views import logout, login


urlpatterns = patterns('',
    url(r'^register/', views.register, name='register'),
    url(r'^login/', login,name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^thanks/',views.thanks,name='thanks'),
)
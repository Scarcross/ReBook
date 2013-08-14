'''
Created on 09.07.2013

@author: leip
'''
from django.conf.urls import patterns,  url
from userauth import views
from django.contrib.auth.views import logout, password_reset,\
    password_change


urlpatterns = patterns('',
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login,name='login'),
    url(r'^logout/', logout,{'next_page':'/main/'}, name='logout'),
    url(r'^thanks/',views.thanks,name='thanks'),
    url(r'^reset/',password_reset,name='pw_reset'),
    url(r'^userarea/',views.userarea,name='userarea'),
    url(r'^userarea/password/',password_reset,{'post_change_redirect':'/main/'},name="pw_reset"),
    url(r'^userarea/password/',password_change,{'post_change_redirect':'/main/'},name="pw_change"),
)
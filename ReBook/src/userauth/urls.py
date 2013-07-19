'''
Created on 09.07.2013

@author: leip
'''
from django.conf.urls import patterns,  url
from userauth import views
from django.contrib.auth.views import logout, login, password_change,\
    password_reset


urlpatterns = patterns('',
    url(r'^register/', views.register, name='register'),
    url(r'^login/', login,name='login'),
    url(r'^logout/', logout,{'next_page':'/main/'}, name='logout'),
    url(r'^thanks/',views.thanks,name='thanks'),
    url(r'^userarea/',views.userarea,name='userarea'),
    url(r'^userarea/password-change/',password_change,{'post_change_redirect':'/main/'},name="pw_change"),
    url(r'^userarea/password-reset/',password_reset,name='pw_reset')
    
)

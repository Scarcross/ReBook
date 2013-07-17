from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ReBook.views.home', name='home'),
#     url(r'^ReBook/', include('ReBook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # Uncomment the next line to enable the admin:
   
    url(r'^$', include("bookshop.urls")),
    url(r'^main/', include("bookshop.urls")),
    
    url(r'^userauth/', include("userauth.urls"))
    
    
   
)

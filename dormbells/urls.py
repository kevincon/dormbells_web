from django.conf.urls.defaults import *

import bell.urls
from local_settings import MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^dormbells/', include('dormbells.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    url(r'^bell/', include(bell.urls)),

    #Browsing
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}, name="homepage"),

    #Account management
    #(r'^account/$', account),
    #(r'^account/edit/$', account_edit),

    #Dormbell management
    #(r'^dormbell/$', dormbell),
    #(r'^dormbell/(\w+)/add$', dormbell_add),
    #(r'^dormbell/(\w+)/edit$', dormbell_edit),

    #Ringer management
    #(r'^ringer/$', ringer),
    #(r'^ringer/add/$', ringer_add),
    #(r'^ringer/(\w+)/edit$', ringer_edit),
   
    #Button management
    #(r'^button/$', button),
    #(r'^button/add/$', button_add),
    #(r'^button/edit/$', button_edit),  

    #Media for CSS 
    url(r'^mymedia/(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': MEDIA_ROOT}),
)

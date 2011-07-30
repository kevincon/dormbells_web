from django.conf.urls.defaults import *

from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #creation
    url(r'^create/confirm$', create_confirm),
    url(r'^create/success$', create_success),

    #deletion
    url(r'^delete/confirm$', delete_confirm),
    url(r'^delete/success$', delete_success),
)

from django.conf.urls.defaults import *

from views import *


urlpatterns = patterns('',
    #creation
    url(r'^create/confirm$', create_confirm),
    url(r'^create/success$', create_success),

    #deletion
    url(r'^delete/confirm$', delete_confirm),
    url(r'^delete/success$', delete_success),
    url(r'^$', index),
)

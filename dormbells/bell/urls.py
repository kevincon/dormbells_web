from django.conf.urls.defaults import *

from views import *


urlpatterns = patterns('',
    #creation
    url(r'^create/confirm/$', create_confirm),

    #deletion
    url(r'^delete/confirm/$', delete_confirm),

    #generic successs
    url(r'^create/success/$', success),
    url(r'^$', index),
)

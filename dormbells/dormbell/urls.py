from django.conf.urls.defaults import *

from views import *


urlpatterns = patterns('',
    #creation
    #url(r'^create/confirm/$', create_confirm),

    #deletion
    #url(r'^delete/confirm/$', delete_confirm),

    #generic successs
    url(r'^success/$', success),
    url(r'^$', index),
    url(r'^(\w{32})$', ringer),
)

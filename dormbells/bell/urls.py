from django.conf.urls.defaults import *

from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^confirm$', confirm),
    url(r'^create_success$', create_success),
)

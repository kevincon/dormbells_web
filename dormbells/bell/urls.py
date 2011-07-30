from django.conf.urls.defaults import *

from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^create/confirm$', confirm),
    url(r'^create/success$', create_success),
)

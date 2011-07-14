from django.conf.urls.defaults import *

urlpatterns = patterns('ring.views',
	(r'^([A-Fa-f0-9]{32})/$', 'ring'),
)

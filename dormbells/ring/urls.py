from django.conf.urls.defaults import *

urlpatterns = patterns('ring.views',
	(r'^(\d+)/$', 'ring'),
)

# Create your views here.
from django.contrib.auth.models import User
from django.http import render_to_response, Http404

def account_page(request, username):
	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		raise Http404(u'Requested user not found.')
	
	

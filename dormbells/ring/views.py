from django.http import HttpResponse

def ring(request, dormbell_id):
	html = "<html><body>You tried to ring dormbell number %s</body></html>" % dormbell_id 
	return HttpResponse(html);

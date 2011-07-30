from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import dormbells.models import *
import datetime
from forms import DormbellCreationForm

def index(request):
    if request.method == 'POST':
	new_dormbell = Dormbell(
	    name = '',
	    user = None,
	    location = '',
	    creation_date = datetime.datetime.now(),
	    consecutive_limit = 0,
	    wait_time_limit = 0,
	    activated=False)
	new_dormbell.save()
	form = DormbellCreationForm(request.POST, {'activated': True}, instance=new_dormbell)
        if form.is_valid():
            #FIXME need to make sure this UUID does not already exist
            new_uuid = uuid.uuid4().hex
            new_button = QRButton(
            	uuid = new_uuid,
            	name = '',  
            	dormbell = new_dormbell,
            	creation_date = datetime.datetime.now())
            new_button.save()
            new_ringer = SMSRinger(
            	name = '',
            	dormbell = new_dormbell,
            	creation_date = datetime.datetime.now(),
           	phone_number = form.cleaned_data['phone_number'],
            	carrier = form.cleaned_data['carrier'])
	    new_ringer.save()
	    form.save()
            return HttpResponseRedirect('/confirm/')
    else:
        form = DormbellCreationForm()
    return render_to_response('index.html', RequestContext(request, {
        'form': form,
    }))

def success(request):
    return HttpResponse("create_success")

def delete_confirm(request):
    return HttpResponse("delete_confirm")

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Dormbell, SMSRinger, QRButton
import datetime
import uuid
from forms import DormbellCreationForm

def index(request):
    print "index view"
    if request.method == 'POST':
	print "post time"
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
	print "about to check if form is valid"
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
	    print "got phone %s and carrier %s" % (new_ringer.phone_number, new_ringer.carrier)
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

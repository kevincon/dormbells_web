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
	form = DormbellCreationForm(request.POST)
	print "about to check if form is valid"
        if form.is_valid():
            print "form was valid"
            request.session['phone_number'] = form.cleaned_data['phone_number']
            request.session['carrier'] = form.cleaned_data['carrier']
	    form.save()
            return HttpResponseRedirect('/confirm/')
        print "form was not valid"
    else:
        form = DormbellCreationForm()
    return render_to_response('index.html', RequestContext(request, {
        'form': form,
    }))

def success(request):
    context = {
        'phone_number': request.session['phone_number'],
        'carrier': request.session['carrier']
    }
    return render_to_response('success.html', RequestContext(request, context))

def ringer(request, uuid):
    button = QRButton.objects.get(uuid=uuid)
    dormbell = button.dormbell
    ringer = dormbell.smsringer_set.all()[0]
    
    return HttpResponse("ring! %s" % ringer.phone_number)

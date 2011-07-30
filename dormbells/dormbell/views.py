from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Dormbell, SMSRinger, QRButton
from carriers import CARRIERS
import datetime
import uuid
import urllib
from forms import DormbellCreationForm

def generate_qr_code(data):
	width = "300"
        height = "300"

        #Google Charts API params
        cht = "qr"
        chs = width + "x" + height
        chl = data
        #chld = "H"

        params = [("cht", cht), ("chs", chs), ("chl", chl)]

        params = urllib.urlencode(params)

	url = "http://chart.apis.google.com/chart?" + params

	return url

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
    #TODO Construct URL for QR Code
    now = datetime.datetime.now()
    new_dormbell = Dormbell(
	name='',
	user=None,
	location='',
	creation_date=now,
	consecutive_limit=0,
	wait_time_limit=0)
    new_dormbell.save()

    new_uuid = uuid.uuid4().hex

    new_button = QRButton(
	name='',
	uuid=new_uuid,
	dormbell=new_dormbell,
	creation_date=now)
    new_button.save()

    new_ringer = SMSRinger(
	name='',
	dormbell=new_dormbell,
	creation_date=now,
	phone_number=request.session['phone_number'],
	carrier=request.session['carrier'])

    new_ringer.save()

    url='http://dormbells.com/%s' % new_uuid 

    context = {
        'qr_code_url': generate_qr_code(url)
    }
    return render_to_response('success.html', RequestContext(request, context))

def ringer(request, uuid):
    button = QRButton.objects.get(uuid=uuid)
    dormbell = button.dormbell
    ringer = SMSRinger.objects.get(dormbell=dormbell)
    ringer.ring()
    return HttpResponse("ring! %s" % ringer.phone_number)

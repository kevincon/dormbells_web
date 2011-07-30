from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import ConfirmationCodeForm


def index(request):
    if request.method == 'POST':
        form = ConfirmationCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/confirm/')
    else:
        form = ConfirmationCodeForm()
    return render_to_response('index.html', RequestContext(request, {
        'form': form,
    }))

def create_confirm(request):
    if request.method == 'POST':
        form = ConfirmationCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bell/success/')
    else:
        form = ConfirmationCodeForm()

    return render_to_response('confirm.html', RequestContext(request, {
        'form': form,
    }))

def success(request):
    return HttpResponse("create_success")

def delete_confirm(request):
    return HttpResponse("delete_confirm")

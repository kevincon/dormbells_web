from models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response

from forms import ConfirmationCodeForm, NumberForm

def index(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            return HttpResponse("valid!")
    else:
        form = NumberForm()
    return render_to_response('index.html', {
        'form': form,
    })

def create_confirm(request):
    if request.method == 'POST':
        form = ConfirmationCodeForm(request.POST)
        if form.is_valid():
            return HttpResponse("valid!")
    else:
        form = ConfirmationCodeForm()
    
    return render_to_response('create_confirm.html', {
        'form': form,
    })

def success(request):
    return HttpResponse("create_success")

def delete_confirm(request):
    return HttpResponse("delete_confirm")

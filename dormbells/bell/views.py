from models import *
from django.http import HttpResponse


def create_confirm(request):
    return HttpResponse("create_confirm")

def create_success(request):
    return HttpResponse("create_success")

def delete_confirm(request):
    return HttpResponse("delete_confirm")

def delete_success(request):
    return HttpResponse("delete_success")

from models import *
from django.http import HttpResponse


def confirm(request):
    return HttpResponse("confirm")

def create_success(request):
    return HttpResponse("success")

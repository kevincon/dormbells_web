from django.contrib.auth.models import User
from django.db import models
from carriers import CARRIERS

class Dormbell(models.Model):
    consecutive_limit = models.IntegerField()
    creation_date = models.DateTimeField()
    location = name = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='dormbells', null=True, blank=True)
    wait_time_limit = models.IntegerField() #in seconds
    activated = models.BooleanField()    

class Button(models.Model):
    class Meta:
        abstract = True

    creation_date = models.DateTimeField()
    dormbell = models.ForeignKey(Dormbell)
    name = models.CharField(max_length=100)
    uuid = models.CharField(max_length=32)

class QRButton(Button):
    pass

class Ringer(models.Model):
    class Meta:
        abstract = True

    creation_date = models.DateTimeField()
    dormbell = models.ForeignKey(Dormbell)
    name = models.CharField(max_length=100)

class EmailRinger(Ringer):
    email = models.EmailField()

class SMSRinger(Ringer):
    phone_number = models.CharField(max_length=20)
    carrier = models.CharField(max_length=40, choices=CARRIERS)


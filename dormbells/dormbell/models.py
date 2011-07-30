from django.template.loader import render_to_string
from django.core.mail import send_mail
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
    address = models.CharField(max_length=50)

    def ring(self):
        title = ""
        message = render_to_string("ring.txt", {})
        #FIXME Construct URL using phone number and carrier for recipients
        constructed_email = self.phone_number + '@txt.att.net'
        recipients = [constructed_email,]#self.cleaned_data['email'],]
        sender = 'Dormbells'
        send_mail(title, message, sender, recipient_list=recipients)

class Empty(models.Model):
	pass

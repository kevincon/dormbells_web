from django.contrib.auth.models import User
from django.db import models
from django_extensions.db import fields


class Dormbell(models.Model):
    consecutive_limit = models.IntegerField()
    creation_date = fields.CreationDateTimeField()
    location = name = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    token = fields.UUIDField()
    user = models.ForeignKey(User, related_name='dormbells', null=True, blank=True)
    wait_time_limit = models.IntegerField() #in seconds
    

class Button(models.Model):
    class Meta:
        abstract = True

    creation_date = fields.CreationDateTimeField()
    dormbell = models.ForeignKey(Dormbell)
    name = models.CharField(max_length=100)


class QRButton(Button):
    pass


class Ringer(models.Model):
    class Meta:
        abstract = True

    creation_date = fields.CreationDateTimeField()
    dormbell = models.ForeignKey(Dormbell)
    name = models.CharField(max_length=100)


class EmailRinger(Ringer):
    email = models.EmailField()


class SMSRinger(Ringer):
    phone_number = models.CharField(max_length=20)



from django.db import models
from django_extensions.db import fields

class Ringer(models.Model):
    class Meta:
        abstract = True

    creation_date = fields.CreationDateTimeField()
    dormbell = models.ForeignKey(Dormbell, related_name='ringers')
    name = models.CharField(max_length=100)

class EmailRinger(Ringer):
    email = models.EmailField()

class SMSRinger(Ringer):
    phone_number = models.CharField(max_length=20)

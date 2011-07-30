from django.db import models
from django_extensions.db import fields

from models import Dormbell

class Button(models.Model):
    class Meta:
        abstract = True

    creation_date = fields.CreationDateTimeField()
    dormbell = models.ForeignKey(Dormbell, related_name='buttons')
    name = models.CharField(max_length=100)


class QRButton(Button):
    pass


class Ring(AuditModel):
    button = models.ForeignKey(Button, related_name='rings')
    ip_address = models.IPAddressField()
    message = models.CharField(max_length=140)
    name = models.CharField(max_length=100)


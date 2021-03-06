from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from dormbells.generic_confirmation.forms import DeferredForm
from models import Dormbell, Empty
from carriers import CARRIERS, LEGEND

class DormbellCreationForm(DeferredForm):
    phone_number = forms.CharField(max_length=20)
    carrier = forms.ChoiceField(choices=CARRIERS)    

    def send_notification(self, user=None, instance=None):
	title = ""
	message = render_to_string("confirm_mail.txt",
				{'token': instance.token, 'user': user})
	#FIXME Construct URL using phone number and carrier for recipients
	constructed_email = self.cleaned_data['phone_number'] + '@' + LEGEND[self.cleaned_data['carrier']]
	recipients = [constructed_email,]#self.cleaned_data['email'],]
	sender = 'Dormbells'
	send_mail(title, message, sender, recipient_list=recipients)

    class Meta:
        model = Empty 
        fields = ('id',) 

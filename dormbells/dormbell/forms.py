from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string


from generic_confirmation.forms import DeferredForm


class ConfirmationCodeForm(DeferredForm):
    def send_notification(self, user=None, instance=None):
        title = "please confirm your new address"
        message = render_to_string("confirm_mail.txt",
                                   {'token': instance.token, 'user': user})
        recipients = [self.cleaned_data['email'],]
        sender = 'from@example.com'
        send_mail(title, message, sender, recipient_list=recipients)

    class Meta:
        model = User #Don't think this will work
        fields = ('email',)

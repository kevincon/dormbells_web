from django import forms

class NumberForm(forms.Form):
    number = forms.CharField()

class ConfirmationCodeForm(forms.Form):
    code = forms.CharField()

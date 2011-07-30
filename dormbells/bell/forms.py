from django import forms

class NumberForm(forms.Form):
    phone_number = forms.CharField(max_length=10)
    CARRIERS = (
        ('AT&T', 'AT&T'),
        ('BOOST', 'Boost Mobile'),
        ('CRICKET', 'Cricket'),
	('METROPCS', 'Metro PCS'),
	('SPRINT', 'Sprint'),
	('TMOBILE', 'T-Mobile'),
	('USCELLULAR', 'US Cellular'),
	('VERIZON', 'Verizon'),
	('VIRGIN', 'VIRGIN MOBILE'),
    )
    carrier = forms.ChoiceField(choices=CARRIERS)

class ConfirmationCodeForm(forms.Form):
    code = forms.CharField(max_length=4)

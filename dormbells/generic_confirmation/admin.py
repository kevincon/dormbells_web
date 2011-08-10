from django.contrib import admin
from dormbells.generic_confirmation.models import DeferredAction

admin.site.register(DeferredAction, 
            list_display=('token', 'valid_until', 'confirmed', 'is_expired'))

from django.contrib import admin
from .models import Event
from .models import participant

# Register your models here.

admin.site.register(Event)
admin.site.register(participant)
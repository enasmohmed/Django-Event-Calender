from django.contrib import admin

# Register your models here.
from eventcalender.models import Event, EventMember

admin.site.register(Event)
admin.site.register(EventMember)
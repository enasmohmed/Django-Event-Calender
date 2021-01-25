from django import forms
from eventcalender.models import EventMember



class AddMemberForm(forms.ModelForm):
  class Meta:
    model = EventMember
    fields = ['user']

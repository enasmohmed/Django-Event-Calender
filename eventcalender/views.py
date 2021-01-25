from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from eventcalender.forms import AddMemberForm
from eventcalender.models import Event, EventMember


# home page
def home(request):
    return render(request, 'home/event_list.html')


# page event list view
class EventListView(ListView):
    model = Event
    template_name = 'home/event_list.html'
    context_object_name = 'eventlist'



# create event view
class EventCreateView(LoginRequiredMixin,CreateView):
    fields = ['title', 'description','date', 'time']
    model = Event
    template_name = 'home/event_form.html'
    success_url ="/event_list/"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(EventCreateView, self).form_valid(form)


# detail view event
@login_required(login_url='accounts:login')
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    eventmember = EventMember.objects.filter(event=event)
    context = {
        'event': event,
        'eventmember': eventmember
    }
    return render(request, 'home/event_detail.html', context)





# update event
class EventUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    fields = ("__all__")
    model = Event
    template_name = 'home/event_form.html'
    success_url ="/event_list/"
    fields = ['title', 'description','date','time']

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.user:
            return True
        return False


# create amount of participants
def add_eventmember(request, event_id):
    forms = AddMemberForm()
    if request.method == 'POST':
        forms = AddMemberForm(request.POST)
        if forms.is_valid():
            member = EventMember.objects.filter(event=event_id)
            event = Event.objects.get(id=event_id)
            if member.count() <= 9:
                user = forms.cleaned_data['user']
                EventMember.objects.create(
                    event=event,
                    user=user
                )
                return redirect('eventcalender:list')
            else:
                print('--------------User limit exceed!-----------------')
    context = {
        'form': forms
    }
    return render(request, 'home/add_member.html', context)


# delete event member
class EventMemberDeleteView(generic.DeleteView):
    model = EventMember
    template_name = 'home/confirm_delete.html'
    success_url = reverse_lazy('eventcalender:list')
    context_object_name = 'member'
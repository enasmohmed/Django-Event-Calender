from django import http
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from eventcalender.models import Event, EventMember


# home page
def home(request):
    return render(request, 'home/index.html')


# page event list view
class EventListView(LoginRequiredMixin,ListView):
    model = Event
    template_name = 'home/event_list.html'
    context_object_name = 'eventlist'


# create event view
class EventCreateView(LoginRequiredMixin,CreateView):
    fields = ['title', 'description','date', 'time']
    model = Event
    template_name = 'home/event_form.html'
    success_url ="/list/"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(EventCreateView, self).form_valid(form)



# detail view event
class EventDetailView(LoginRequiredMixin,DetailView):
    model = Event
    context_object_name = 'event_detail'
    template_name = 'home/event_detail.html'
    #
    # def get_queryset(self):
    #     return EventMember.objects.filter(user=self.kwargs['pk']).order_by('user')




# update event
class EventUpdateView(LoginRequiredMixin,UpdateView):
    fields = ("__all__")
    model = Event
    template_name = 'home/event_form.html'
    success_url ="/list/"
    fields = ['title', 'description','date','time']



# delete event
class EventDeleteView(LoginRequiredMixin,DeleteView):
    model = Event
    template_name = 'home/confirm_delete.html'
    success_url = "/list/"


# create event member
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
                return redirect('eventcalender:home')
            else:
                print('--------------User limit exceed!-----------------')
    context = {
        'form': forms
    }
    return render(request, 'home/add_member.html', context)



class EventMemberDeleteView(generic.DeleteView):
    model = EventMember
    template_name = 'home/confirm_delete.html'
    success_url = reverse_lazy('eventcalender:home')
    slug_field = 'event_id'
    slug_url_kwarg = 'event_id'

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

# Create your views here.
from . models import Event


def index(request):
    return render(request, 'event/index.html')



class EventList(ListView):
    model = Event



class EventDetail(DetailView):
    model = Event
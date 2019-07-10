from django.shortcuts import render
from .models import Event
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


class Event_List(ListView):

    model = Event
    template_name = 'event/list.html'


class Event_Detail(DetailView):

    model = Event
    template_name = 'event/detail.html'

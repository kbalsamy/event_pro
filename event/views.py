from django.shortcuts import render
from .models import Event, Hall
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse

# Create your views here.


class Event_List(ListView):

    model = Event
    template_name = 'event/list.html'


class Event_Detail(DetailView):

    model = Event
    template_name = 'event/detail.html'


def get_price(request):

    hall_id = request.GET.get('hall_id', None)
    event = request.GET.get('event', None)
    hall = Hall.objects.get(hall_id=hall_id, event__name=event)
    data = {
        'hall_id': hall.hall_id,
        'price': str(hall.price)
    }
    return JsonResponse(data)

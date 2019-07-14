from django.shortcuts import render, redirect
from .models import Event, Hall
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .cart import Cart
from orders.forms import OrderCreateForm

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


@require_POST
def checkout_view(request, event):

    cart = Cart(request)
    data = request.POST.get('hall_id')
    hall_ids = list(data.split(','))
    cart.add(hall_ids, event)
    form = OrderCreateForm()
    return render(request, 'event/checkout.html', {'cart': cart, 'form': form})

from django.shortcuts import render, redirect
from django.urls import reverse
from event.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItems
from django.views.decorators.http import require_POST

# Create your views here.


@require_POST
def order_create(request):

    cart = Cart(request)

    if request.method == 'POST':

        form = OrderCreateForm(request.POST)

        if form.is_valid():

            order = form.save()

            for item in cart:

                OrderItems.objects.create(order=order, hall_id=item['hall_id'], event=item['event'], price=item['price'])

                cart.clear()

                request.session['order_id'] = order.id

                return redirect(reverse('payments:process'))

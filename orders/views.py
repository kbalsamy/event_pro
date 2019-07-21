from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from event.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItems, Order
from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required

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


@staff_member_required
def admin_order_detail(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    return render(request, 'admin/orders/order/detail.html', {'order': order})

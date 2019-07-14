from django.shortcuts import render, redirect, get_object_or_404
import braintree
from orders.models import Order
from django.conf import settings
from braintree import Configuration, Environment


gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=settings.BRAINTREE_MERCHANT_ID,
        public_key=settings.BRAINTREE_PUBLIC_KEY,
        private_key=settings.BRAINTREE_PRIVATE_KEY
    )
)


def payment_process(request):

    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':

        nonce = request.POST.get('payment_method_nonce', None)

        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_order_cost()),
            'payment_method_noncey': nonce,
            'options': {'submit_for_settlement': True}
        })

        if result.is_success:

            order.paid = True

            order.braintree_id = result.transaction.id

            order.save()

            return redirect('payments:done')
        else:
            return redirect('payments:cancelled')

    else:

        client_token = gateway.client_token.generate()

        return render(request, 'payments/process.html', {'order': order, 'client_token': client_token})


def payment_done(request):

    return render(request, 'payments/payment_done.html')


def payment_cancelled(request):

    return render(request, 'payments/payment_cancelled.html')

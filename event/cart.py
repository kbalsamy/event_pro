from decimal import Decimal
from django.conf import settings
from .models import Hall
from django.forms.models import model_to_dict


class Cart():

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, hall_id, event):

        halls = Hall.objects.filter(event__name=event, available=True)

        for id in hall_id:
            if id not in self.cart:
                selected_hall = halls.get(hall_id=id)
                if selected_hall:
                    price = halls.get(hall_id=id).price
                    self.cart[id] = {'hall_id': id, 'price': str(price), 'event': event}

        self.save()

    def save(self):

        self.session.modified = True

    def remove(self, hall_id):

        if hall_id in self.cart:
            del self.cart[hall_id]
            self.save()

    def __iter__(self):

        # work later

        hall_ids = self.cart.keys()
        halls = Hall.objects.filter(hall_id__in=hall_ids)

        cart = self.cart.copy()

        for item in cart.values():

            item['total_price'] = item['price'] * len(cart)
            yield item

    def __len__(self):

        return len(self.cart)

    def get_total(self):

        return sum(Decimal(item['price']) for item in self.cart.values())

    def show_cart(self):

        return self.cart

    def clear(self):

        del self.session[settings.CART_SESSION_ID]

        self.save()

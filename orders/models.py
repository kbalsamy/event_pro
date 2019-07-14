from django.db import models
from event.models import Hall
# Create your models here.


class Order(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)

    def __str(self):

        return str(self.id)

    def get_total_order_cost(self):

        return sum(item.get_cost for item in self.items.all())


class OrderItems(models.Model):

    order = models.ForeignKey(Order, related_name='itemds', on_delete=models.CASCADE)
    hall_id = models.CharField(max_length=10)
    event = models.CharField(max_length=20, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):

        return str(self.id)

    def get_cost(self):

        return self.price

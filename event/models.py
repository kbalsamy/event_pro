from django.db import models
from django.urls import reverse


def allocate_file_name(instance, filename):

    return "{}_{}".format(instance.name, filename)


# Create your models here.
class Catagory(models.Model):

    " this table clasifies the event types"

    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)

    def __str__(self):

        return self.name


class Layout(models.Model):

    name = models.CharField(max_length=50, blank=True)
    layout_map = models.FileField(upload_to=allocate_file_name, blank=True)
    layout_price_plan = models.FileField(upload_to=allocate_file_name, blank=True)
    allocated = models.PositiveIntegerField(default=1)

    def __str__(self):

        return self.name


class Event(models.Model):

    "This table provides all info about the event, one layout for Many Events"

    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    conducted_on = models.DateField()
    description = models.TextField()
    layout = models.ForeignKey('Layout', related_name='layout', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    catagory = models.ForeignKey(Catagory, related_name='catagory', on_delete=models.CASCADE)

    def __str__(self):

        return self.slug + self.conducted_on.strftime('%Y-%m-%d')

    def get_absoulte_url(self):

        pass


class Hall(models.Model):

    types = [('small', 'SMALL'), ('large', 'LARGE')]

    hall_id = models.CharField(max_length=5)
    hall_type = models.CharField(max_length=10, choices=types)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    event = models.ForeignKey(Event, related_name='event', on_delete=models.CASCADE)

    def __str__(self):

        return self.hall_id

from django.db import models
from django.urls import reverse

# Create your models here.


class Catagory(models.Model):

    " this table clasifies the event types"

    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)

    def __str__(self):

        return self.name


class Event(models.Model):

    "This table provides all info about the event "

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


class Layout(models.Model):

    plan = models.TextField(blank=True)
    allocated = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000)

    def __str__(self):

        return str(self.id)

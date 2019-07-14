from django.contrib import admin
from .models import Order, OrderItems


# Register your models here.

class OrderItemInline(admin.TabularInline):

    model = OrderItems

    raw_id_fields = ['order']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ['first_name', 'last_name', 'email', 'paid']

    inlines = [OrderItemInline]

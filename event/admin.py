from django.contrib import admin
from .models import Event, Catagory, Layout, Hall

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ['name', 'location', 'conducted_on', 'created']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Layout)
admin.site.register(Hall)

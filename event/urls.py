from django.urls import path
from .views import Event_List, Event_Detail, get_price, checkout_view
from django.conf.urls import url

app_name = 'event'


urlpatterns = [path('event_list', Event_List.as_view(), name='event_list'),
               path('<int:id>/<slug:slug>/', Event_Detail.as_view(), name='event_detail'),
               url(r'ajax/get_price/$', get_price, name='hall_price'),
               path('checkout/<str:event>/', checkout_view, name='checkout')
               ]

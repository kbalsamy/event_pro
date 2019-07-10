from django.urls import path
from .views import Event_List, Event_Detail

app_name = 'event'


urlpatterns = [path('event_list', Event_List.as_view(), name='event_list'),
               path('<int:id>/<slug:slug>/', Event_Detail.as_view(), name='event_detail'),
               ]

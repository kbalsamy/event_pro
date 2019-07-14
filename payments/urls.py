from django.urls import path

from .views import payment_process, payment_done, payment_cancelled


app_name = 'payments'


urlpatterns = [path('process/', payment_process, name='process'),
               path('done/', payment_done, name='done'),
               path('cancelled/', payment_cancelled, name='cancelled'),
               ]

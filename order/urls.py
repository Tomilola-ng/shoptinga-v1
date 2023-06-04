from django.urls import path
from .views import start_order,cancel_view
from cart.views import success_view
urlpatterns = [
     path('start_order/',start_order,name='start_order'),
     path('purchased/loading',success_view, name='payment-successful'),
]
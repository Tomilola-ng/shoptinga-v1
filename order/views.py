from django.shortcuts import render,redirect,reverse
from .models import Order,Orderitem
from cart.cart import Cart
from coinbase_commerce.client import Client
from shoptinga import settings
from django.http import JsonResponse, HttpResponse
import requests
import paystack
from django.contrib import messages

def start_order(request):
	return render(request, 'cart/checkout.html', context)





def cancel_view(request):
    return render(request, 'cart/cancel.html', {'public_key': settings.PAYSTACK_PUBLIC_KEY})
    
	

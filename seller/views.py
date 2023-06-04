from django.shortcuts import render,get_object_or_404,redirect
from django.http.response import JsonResponse
from json.decoder import JSONDecodeError
import os
from django.urls import reverse
from seller.models import Shop
from django.http import HttpResponseRedirect, HttpResponse
import requests
from order.models import Orderitem, Order
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from product.models import Product
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

@login_required
def index(request):
    shops = Shop.objects.filter(user=request.user)
    return render(request, "seller/index.html", {
        "shops": shops
    })

@login_required
def create_shop(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        logo = request.FILES.get('logo')
        category = request.POST['category']
        phone = request.POST['phone']
        email = request.POST['email']
        country  = request.POST['country']
        bank_name  = request.POST['bank_name']
        bank_acct = request.POST['bank_acct']
        w_address  = request.POST['w_address']
        
        if Shop.objects.filter(name=name).exists():
            messages.error(request, 'A creator account with the unique name already exist.')
            return redirect('create-shop')
     	    
        Shop(name=name, description=description, logo=logo,phone=phone,email=email,bank_name=bank_name,bank_acct=bank_acct,country=country,w_address=w_address,category=category,user=request.user).save()
        return redirect("sellers")
    else:
     	  	return render(request, "seller/create-shop.html")
     	  	         
def add_item(request,shop_id):
	if request.method == 'POST':
		name=request.POST["name"]
		description = request.POST["description"]
		price = float(request.POST["price"])
		image = request.FILES.get('image')
		thumbnail = request.FILES.get('thumbnail')
		content = request.FILES.get('content')
		Product(name=name, description=description, price=price,image=image,thumbnail=thumbnail,content=content,shop_id=shop_id).save()
		product = Product.objects.filter(name=request.POST["name"], description=request.POST["description"], price=float(request.POST["price"]), shop_id=shop_id)[::-1][0]
		
		return HttpResponseRedirect(f"/seller/shop/{shop_id}/")
	else:
		return render(request, "seller/add-item.html")
		
def view_item(request, shop_id, product_id):
    shop = Shop.objects.get(shop_id=shop_id)
    product = Product.objects.get(product_id=product_id)

    return render(request, "seller/view-item.html", {
        "shop": shop,
        "product": product,
    })

"""
    Function View
"""

def view_shop(request, shop_id):
    shop = get_object_or_404(Shop,shop_id=shop_id)
    products = Product.objects.filter(shop_id=shop_id)
    data = []

    for product in products:
        order = Orderitem.objects.filter(item_id=product.product_id)
        if len(order) != 0:
            data.append([o for o in order])

    items_data = []

    return render(request, "seller/shop.html", {
        "data": data,
        "data_length": len(data),
        "items": items_data,
        "shop":shop,
        "products":products,
    })

def view_orders(request, shop_id):
    products = Product.objects.filter(shop_id=shop_id)
    data = []

    for product in products:
        order = Orderitem.objects.filter(item_id=product.product_id)
        if len(order) != 0:
            data.append([o for o in order])

    print(data)

    return render(request, "seller/orders.html", {
        "data": data,
        "data_length": len(data)
    })
    
def view_order(request, shop_id, order_item):
    order_item_2 = OrderItem.objects.get(id=order_item)
    order = Order.objects.get(payment_id=order_item_2.payment_id)
    user = User.objects.get(id=order.user_id)
    profile = Profile.objects.get(user_id=order.user_id)
    item = Item.objects.get(item_id=order_item_2.item_id)


    return render(request, "seller/order.html", {
        "order_item": order_item_2,
        "order": order,
        "profile": profile,
        "item": item,
        "user": user
    })

class ProductDeleteView(DeleteView):
	model = Product
	success_url = '/seller'
	template_name = 'seller/confirm_delete.html'
	

class ProductUpdateView(UpdateView):
	model = Product
	fields = ['name', 'image','thumbnail','price','description','content']
	template_name = 'seller/product_update.html'
	success_url = '/seller'

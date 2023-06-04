from django.conf import settings
from django.shortcuts import render,redirect
from .cart import Cart
from django.contrib.auth.decorators import login_required
from product.models import Product
from coinbase_commerce.client import Client
from order.models import Order,Orderitem
from seller.models import Shop
from django.contrib import messages




# VIEWS FUNCTIONS
def add_to_cart(request, product_id):
	cart = Cart(request)
	cart.add(product_id)
	return render(request,'cart/partials/menu_cart.html')
	

def cart(request):
	return render(request,'cart/cart.html')
	

def update_cart(request, product_id, action):
	cart = Cart(request)
	if action == 'increment':
		cart.add(product_id,1,True)
	else:
		cart.add(product_id,-1,True)
	product = Product.objects.get(pk=product_id)
	quantity = cart.get_item(product_id)
	if quantity:
		quantity = quantity['quantity']
		item = {
	        'product':{
	                'id':product.id,
	                'name':product.name,
	                'image':product.image,
	                'price':product.price,
	        },
	        "total_price": (quantity * product.price),
	        "quantity":quantity,
	}
	else:
		item = None
	response = render(request,'cart/partials/cart_item.html',{'item':item})
	response['HX-Trigger'] = 'update-menu-cart'
	return response
	

@login_required
def checkout(request):
	client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
	cart = Cart(request)
	total_price = 0
	 
	for item in cart:
		product = item['product']
		total_price += product.price * int(item['quantity'])
		domain_url = 'http://localhost:8000/'
	charge_data = {
        'name': 'shoptinga',
        'description': 'payment for products',
        'local_price': {
            'amount': total_price,
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url + 'order/purchased',
        'cancel_url': domain_url + 'cancel/',
    }
	charge = client.charge.create(**charge_data)
		
	return render(request,'cart/checkout.html',{
	'charge':charge})	  


def hx_menu_cart(request):
	return render(request,'cart/partials/menu_cart.html')
	

def hx_cart_total(request):
	return render(request,'cart/partials/cart_total.html')


def success_view(request):
	cart = Cart(request)
	total_price = 0
    
	for item in cart:
		product = item['product']
		total_price += product.price * int(item['quantity'])
	order = Order.objects.create(user=request.user)

	order.paid_amount = total_price
	order.paid = True
	order.save()
	
	for item in cart:
		product = item['product']
		quantity = int(item['quantity'])
		price = product.price * quantity
		item = Orderitem.objects.create(order=order,product=product,price=price,quantity=quantity,item_id=product.product_id,paid=True)
		product_seller = Shop.objects.get(shop_id = product.shop_id)
		product_seller.balance += item.price - ( item.price * (product_seller.commision / 100))
		product_seller.save()

	cart.clear()
	return redirect("myaccount")
	
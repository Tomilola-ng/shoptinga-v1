from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import render,redirect
from product.models import Product,Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

def frontpage(request):
	products = Product.objects.filter(approved=True)[0:8]
	return render(request,'core/frontpage.html',{'products':products})

def shop(request):
	categories = Category.objects.all()
	products = Product.objects.filter(approved=True)
	active_category = request.GET.get('category','')
	if active_category:
		products = products.filter(category__slug=active_category)
	
	query = request.GET.get('query','')
	
	if query:
		products = products.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query))
	context = {
	         'categories':categories,
	         'products':products,
	         'active_category':active_category,
	}
	return render(request,'core/shop.html',context)

    	
def page_not_found_view(request, exception):
    return render(request, 'core/404.html')
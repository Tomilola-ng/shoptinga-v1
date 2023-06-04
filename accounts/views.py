from django.shortcuts import render, redirect
from .forms import SignUpForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
from seller.models import Shop

# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		
		if form.is_valid():
			email = form.cleaned_data.get('email')
			if User.objects.filter(email=email).exists():
				messages.error(request, 'This email address is already in use.')
				return redirect('signup')
			user = form.save()
			messages.success(request, 'You have started your buying/selling journey with crypto and money ' )
			login(request, user)
			return redirect('myaccount')
	else:
		form = SignUpForm()
	return render(request,'accounts/signup.html',{'form': form})
 
def profile(request):
	if request.method == 'POST':
		p_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
		if p_form.is_valid():
			p_form.save()
			return redirect('/')
	else:
		p_form = ProfileUpdateForm(instance=request.user.profile)
		context = {
	    	'p_form' : p_form
	    }
		return render(request, 'accounts/myinfo.html', context)
    
def login_access(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('shop')
		else:
			return HttpResponse('Invalid login credentials')
	else:
		return render(request, 'accounts/login.html')

	return render(request,'accounts/login.html')
@login_required
def myaccount(request):
	return render(request,'accounts/myaccount.html')
	
@login_required
def edit_myaccount(request):
	if request.method == 'POST':
		user = request.user
		user.first_name = request.POST.get('first_name')
		user.last_name = request.POST.get('last_name')
		user.username = request.POST.get('username')
		user.email = request.POST.get('email')
		user.save()
		
		return redirect('myaccount')
	return render(request,'accounts/edit_myaccount.html')

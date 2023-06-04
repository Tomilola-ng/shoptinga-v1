from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
	email= forms.EmailField(max_length=250,required=True)
	first_name=forms.CharField(max_length=255,required=True)
	last_name=forms.CharField(max_length=255,required=True)
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']
	
	
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['country','phone']
	 	
	 	

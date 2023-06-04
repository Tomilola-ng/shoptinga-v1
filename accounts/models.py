from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	country = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	
	def __str__(self):
		return f'{self.user.username} Profile'
		
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
	
# Create your models here.

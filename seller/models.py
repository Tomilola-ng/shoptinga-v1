from django.db import models
import uuid
from django.core.files import File
from shoptinga.util import unique_slug_generator
from six import python_2_unicode_compatible
from django.dispatch import receiver
from django.db.models.signals import pre_save
from PIL import Image
from io import BytesIO
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Shop(models.Model):
    user = models.ForeignKey(User,related_name="shops",on_delete=models.CASCADE)
    shop_id = models.UUIDField(default=uuid.uuid4, unique=True)
    balance = models.FloatField(default=0)
    commision = models.IntegerField(default=3)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=225)
    logo = models.ImageField(upload_to="logo,")
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255,blank=True,null=True)
    bank_acct = models.CharField(max_length=15,blank=True,null=True)
    w_address = models.CharField(max_length=225,blank=True,null=True)
    approved = models.BooleanField(default=False)
    
    def __str__(self):
    	return self.name
    

	


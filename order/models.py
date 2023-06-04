from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from product.models import Product
from django.conf import settings
class Order(models.Model):
	user = models.ForeignKey(User,related_name='orders',blank=True,null=True,on_delete = models.CASCADE)	
	created_at = models.DateTimeField(auto_now_add=True)
	paid = models.BooleanField(default=False)
	paid_amount = models.IntegerField(blank=True,null=True)
	
	class Meta:
		ordering = ['-created_at',]
	def get_total_price(self):
		if self.paid_amount:
			return self.paid_amount
		return 0
		
class Orderitem(models.Model):
	item_id = models.UUIDField()
	paid = models.BooleanField(default=False)
	order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
	product= models.ForeignKey(Product,related_name='items',on_delete=models.CASCADE)
	price = models.IntegerField()
	quantity = models.IntegerField(default=1)
	
	def get_total_price(self):
		return self.price
		
# Create your models here.

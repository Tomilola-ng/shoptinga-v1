from django.db import models
from django.core.files import File
from shoptinga.util import unique_slug_generator
from six import python_2_unicode_compatible
from django.dispatch import receiver
from django.db.models.signals import pre_save
from PIL import Image
from io import BytesIO
from cloudinary.models import CloudinaryField
import cloudinary.uploader
import uuid
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField()
	
	class Meta:
		ordering = ['name',]
		verbose_name_plural = 'categories'
	def __str__(self):
		return self.name
	
class Product(models.Model):
	product_id = models.UUIDField(default=uuid.uuid4)
	shop_id = models.UUIDField()
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255,blank=True,null=True)
	image = models.ImageField(upload_to="products,")
	thumbnail = models.ImageField(upload_to="products,", blank=True, null=True)
	content = models.FileField(upload_to="content", blank=True,null=True)
	description = models.TextField(blank=True, null=True)
	membership = models.URLField(blank=True,null=True)
	price = models.FloatField()
	category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE,blank=True,null=True)
	approved = models.BooleanField(default=False)
	created_at= models.DateTimeField(auto_now_add=True)
	
	def get_absolute_url(self):
		return ('shop')
	
	class Meta:
		ordering = ['-created_at',]
	def __str__(self):
		return self.name
		
	def get_thumbnail(self):
		if self.thumbnail:
			return self.thumbnail.url
		else:
			if self.image:
				self.thumbnail = self.make_thumbnail(self.image)
				self.save()
				
				return self.thumbnail_url
				
	def make_thumbnail(self, image, size =(300, 300)):
			img = Image.open(image)
			img.convert('RGB')
			img.thumbnail('size')
			
			thumb_io = BytesIO()
			img.save(thumb_io, 'JEPG', quality=85)
			
			thumbnail = File(thumb_io, name=image.name)
			return thumbnail
			
	def get_rating(self):
			reviews_total = 0
			
			for review in self.reviews.all():
				reviews_total += review.rating
			
			if reviews_total > 0:
				return reviews_total/ self.reviews.count()
			return 0
			
			
class Review(models.Model):
	product = models.ForeignKey(Product, related_name='reviews', on_delete= models.CASCADE)
	rating = models.IntegerField(default=3)
	comment = models.TextField()
	created_by = models.ForeignKey(User, related_name='reviews', on_delete= models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)		
	
		


	
@receiver(pre_save, sender=Product)
def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)	
# Create your models here.

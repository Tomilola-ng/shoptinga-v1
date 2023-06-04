from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Review
from coinbase_commerce.client import Client
from shoptinga import settings
def product(request, slug):
	product = get_object_or_404(Product,slug=slug)
	if request.method=='POST':
		rating = request.POST.get('rating',3)
		content = request.POST.get('content','')
		if content:
			reviews = Review.objects.filter(created_by=request.user,product=product)
			if reviews.count() > 0:
				review = reviews.first()
				review.rating = rating
				review.content = content
				review.save()
			else:
				review = Review.objects.create(product=product,
				rating=rating,
				comment=content,
				created_by=request.user)
			return redirect('product',slug=slug)
			
	return render(request,'product/product.html',{'product':product})


def cancel_view(request):
    return render(request, 'cart/cancel.html', {})
# Create your views here.

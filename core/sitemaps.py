from django.contrib.sitemaps import Sitemap
from product.models import Product

class PostSitemap(Sitemap):
		changefreq = "weekly"
		priority = 0.9
		
		def items(self):
				return Product.objects.filter(approved=True)
		
		def lastmod(self, obj):
				return obj.created_at
from django.contrib import admin
from .models import Order,Orderitem
class OrderItemInline(admin.TabularInline):
	model = Orderitem
	row_id_fields = ['product']
	
class OrderAdmin(admin.ModelAdmin):
	list = ['id','created_at']
	list_filter = ['paid','created_at']
	search_fields = ['id','user','created_at']
	inlines = [OrderItemInline]
admin.site.register(Order, OrderAdmin)
admin.site.register(Orderitem)
# Register your models here.

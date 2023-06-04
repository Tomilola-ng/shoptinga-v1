from django.contrib import admin
from .models import Shop
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name','country','phone','logo','email','approved','w_address','bank_name','bank_acct')
    list_filter = ('approved','name')
    search_fields = ('name', 'email')
    actions = ['approve_shop']

    def approve_shop(self, request, queryset):
        queryset.update(approved)

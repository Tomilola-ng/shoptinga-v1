from django.urls import path
from core.views import frontpage,shop
from product.views import product,cancel_view
urlpatterns = [
    path('',frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
     path('shop/<slug:slug>/', product, name='product'),
    path('cancel/', cancel_view, name='payments-cancel'),
]

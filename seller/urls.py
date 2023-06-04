from django.urls import path
from . import views
from .views import ProductDeleteView,ProductUpdateView

urlpatterns = [
    path("", views.index,name='sellers'),
    path("create-shop/", views.create_shop, name="create-shop"),
    path("shop/<uuid:shop_id>/add-item/", views.add_item),
    path("shop/<uuid:shop_id>/items/<uuid:product_id>/", views.view_item),
    path("shop/<uuid:shop_id>/", views.view_shop,name="dashboard"),
    path("shop/<uuid:shop_id>/orders/", views.view_orders),
    path("shop/<uuid:shop_id>/orders/<str:order_item>/", views.view_order),
    path('shop/<uuid:shop_id>/<slug:slug>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('shop/<uuid:shop_id>/<slug:slug>/update', ProductUpdateView.as_view(), name='product-update'),
]
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import PostSitemap
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from two_factor.urls import urlpatterns as tf_urls

sitemaps = {
		"posts": PostSitemap,
}
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('', include(tf_urls)),
    path('account/',include('accounts.urls')),
    path('cart/',include('cart.urls')),
    path('order/',include('order.urls')),
    path('seller/',include('seller.urls')),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='core/password_reset.html'),name='password_reset'),
     path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'),name='password_reset_done'),
     path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'),name='password_reset_complete'),
      path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html'),name='password_reset_confirm'),
    path('sitemap.xml', sitemap,{'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]
handler404 = "core.views.page_not_found_view"

if settings.DEBUG:
	
    urlpatterns +=static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

from django.urls import path
from accounts.views import signup,myaccount,edit_myaccount,profile,login_access
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('logout/', auth_views.LogoutView.as_view(),name="logout" ),
    path('signup/', signup, name="signup"),
    path('login/',auth_views.LoginView.as_view(template_name="core/login.html"),name="login"),
    path('myinfo/', profile, name='myinfo'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit/', edit_myaccount, name='edit_myaccount'),

]
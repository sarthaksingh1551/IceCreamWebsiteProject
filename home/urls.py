from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('menu',views.menu, name = 'menu'),
    path('about',views.about, name = 'about'),
    path('contacts',views.contacts, name = 'contacts'),
    path('signup',views.handleSignup, name = 'handleSignup'),
    path('login',views.handleLogin, name = 'handleLogin'),
    path('logout',views.handleLogout, name = 'handleLogout'),

]

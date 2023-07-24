from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('products', views.products, name='products'),
     path('detail/<str:id>', views.detail, name='detail'),
     path('category/<str:id>/<slug:slug>', views.category, name='category'),
     path('contact', views.contact, name='contact'),
     path('signout', views.signout, name='signout'),
     path('signin', views.signin, name='signin'),
     path('register', views.register, name='register'),
     path('profile', views.profile, name='profile'),
     path('profile_update', views.profile_update, name='profile_update'),
     path('password_update', views.password_update, name='password_update'),
    
    

]

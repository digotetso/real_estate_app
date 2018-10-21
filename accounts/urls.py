from django.urls import path
from . import  views

urlpatterns = [
    path('register', views.register, name ='register'),
    path('login', views.login, name ='login'),#add parameter
    path('logout', views.logout, name ='logout'),
    path('dashboard', views.dashboard, name ='dashboard')
    
]
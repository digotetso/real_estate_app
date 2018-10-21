from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name ='listings'),
    path('<int:listing_id>', views.listing, name ='listing'),#add parameter
    path('search', views.search, name ='search')
    
]
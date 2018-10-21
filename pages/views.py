from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.models import Realtor
from listings.choices import price_choices,state_choice,bedroom_choices

def index (requests):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'state_choices': state_choice,
        'bedrooms_choices': bedroom_choices
    }
    return render(requests, 'pages/index.html', context) # it will look for index.html in templates folder

def about (requests):
    #Get all realtors from db
    realtors = Realtor.objects.order_by('-hire_date')

    #Get MVP from db
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True) # [:1]

    context = {
        'realtors' : realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(requests, 'pages/about.html', context) # it will look for index.html in templates folder

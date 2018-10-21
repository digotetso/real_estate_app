from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choices import price_choices,state_choice,bedroom_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) #get listings from db
    paginator = Paginator(listings, 6)  #three listings per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)
    

def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):

###########Query set #########################
    queryset_list = Listing.objects.order_by('-list_date')

    #Keyword search
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']   # http://localhost:8000/listings/search?keywords=pool --> get keywords from req url
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    #City search
    if 'city' in request.GET:
        city = request.GET['city']   # get city from req url
        if city:
            queryset_list = queryset_list.filter(city__iexact=city) #iexact -->case insesitive, exact--->case sensitive

    #State search
    if 'state' in request.GET:
        state = request.GET['state']   # get state from req url
        if state:
            queryset_list = queryset_list.filter(state__exact=state)

    #price search
    if 'price' in request.GET:
        price = request.GET['price']   # get price from req url
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    
    #bedrooms search
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']   # get bedrooms from req url
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)


    context = {
        'listings': queryset_list,
        'price_choices': price_choices,
        'state_choices': state_choice,
        'bedrooms_choices': bedroom_choices,
        'values' : request.GET
       }
    return render(request, 'listings/search.html', context)
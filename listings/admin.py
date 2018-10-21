from django.contrib import admin

# Register your models here.
from .models import Listing

#To customise admin
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor') # things tha i want it to display in admin page
    list_display_links = ('id', 'title') # to make id and title clickable
    list_filter = ('realtor',) #add extra box for filtering
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'city', 'state', 'zipcode', 'price', 'address')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)

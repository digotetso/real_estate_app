from django.contrib import admin

# Register your models here.
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hire_date') # things tha i want it to display in admin page
    list_display_links = ('id', 'name') # to make id and title clickable
    search_fields = ('name', )
    list_per_page = 25
 

admin.site.register(Realtor,RealtorAdmin)

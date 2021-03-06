from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail 
# Create your views here.


def contacts(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']        
        listing = request.POST['listing']
        phone = request.POST['phone']        
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #check of user has already inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have laready made inquiry for this is listing')
                return redirect('/listings/'+listing_id)



        contact = Contact(listing=listing, listing_id=listing_id, name=name,email=email,
                          phone=phone,message=message,user_id=user_id)

        contact.save()
        send_mail(
            'Property Listing Inquiry',
            'There has been an iv nquiry for ' + listing,
            'pro.digmatema@gmail.com',
            [realtor_email, 'digotetso.matema@mascom.bw', 'pro.digmatema@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'You request  is submitted for processing, we will get back to you')
        
        return redirect('/listings/'+listing_id)

    return redirect('/listings/'+listing_id)

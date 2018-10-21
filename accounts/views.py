from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.

def register(request):
    if request.method == 'POST':
        #messages.error(request, 'Testing error message')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        #check password match ?
        if password == password2:
            #Check is username is unique
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('register')
            else: 
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email is taken')
                    return redirect('register')
                else:
                    #then we can register a user
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                    last_name=last_name)

                    #login after register  -->
                    # use auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    #return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered')
                    return redirect('login')


        else:
            messages.error(request, 'passwords do not match')  
            return redirect('register')     

    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':  
        password = request.POST['password']
        username = request.POST['username']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'your credintials are incorrect')   
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
    

def logout(request):
    if request.method == 'POST':  
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard (request):
    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contact
    }

    return render(request, 'accounts/dashboard.html', context)


from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Sent Successfully.')
        
    return render(request, 'contacts.html')

def signup(request):
    if request.method == "POST":
        # Get the post parameters
        print(type(request.POST))
        print(request.POST.keys())
        print(request.POST)
        fname = request.POST('fname')
        lname = request.POST('lname')
        username = request.POST('username')
        email = request.POST('email')
        pass1 = request.POST('pass1')
        pass2 = request.POST('pass2')

        # Check for errors

        # Create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.firstname = fname
        myuser.lastname = lname
        myuser.save()
        messages.success(request, 'Account has been created successfully.')
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found')
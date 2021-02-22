from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import Contact

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    if request.method == "POST":
        print("a", type(request.POST))
        print("b", request.POST.keys())
        print("c", request.POST)
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Sent Successfully.')
        
    return render(request, 'contacts.html')

def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST["loginusername"]
        loginpass = request.POST["loginpass"]

        User = authenticate(request, username=loginusername, password=loginpass)

        if User is not None:
            print("logged in")
            login(request, User)
            messages.success(request, "Logged in Successfully.")
            return redirect("home")

        else:
            messages.error(request, "Invalid Credentials.")
            return redirect("home")
    else:
        return HttpResponse("404 - Not Found")

def handleLogout(request):
    return redirect("home")

def handleSignup(request):
    if request.method == "POST":
        # Get the post parameters
        print(type(request.POST))
        print(request.POST.keys())
        print(request.POST)
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        # Check for errors
        if len(username) >12:
            print("username error")
            messages.error(request, 'Username must be under 12 characters.')
            return redirect('home')

        if not username.isalnum():
            print("username error2")
            messages.error(request, 'Username must atleast contain one number.')
            return redirect('home')

        if pass1!=pass2:
            print("pass error")
            messages.error(request, 'Password does not match.')
            return redirect('home')

        # Create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Account has been created successfully.")
        return redirect("home")

    else:
        return HttpResponse("404 - Not Found")
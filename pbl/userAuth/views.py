from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
import re
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    if request.user.is_authenticated:
        return render (request, 'userAuth/index.html')
    else:
        return redirect("login")

def entry(request):
    return render(request, 'userAuth/idx.html')

def menu(request):
    return render(request, 'userAuth/menuu.html')

def userRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        rep_password = request.POST['rep_password']
        email = request.POST['email']

        if User.objects.filter(username = username).exists():
            messages.error(request, "User already exists!")
            return redirect("register")
        else:
            if password == rep_password and len(username)>3 and len(password)>8: 
                if re.search('[A-Z]', password)!=None and re.search('[0-9]', password)!=None and re.search("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$", password)!=None:
                    user = User.objects.create_user(username = username, email = email, password = password)
                    user.save()
                    messages.success(request, "User creation successful! Kindly proceed for login")
                    return redirect("login")
                else:
                    messages.error(request, "Enter valid credentials")
                    return redirect("register")
            else:
                messages.error(request, "User registration failed!")
                return redirect("register")
    return render(request, 'userAuth/register.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Login Failed due to invalid credentials!")
            return redirect("login")
    return render(request, 'userAuth/login.html')

def userLogout(request):
    logout(request)
    return redirect("login")

def NA(request):
    return render(request, 'userAuth/NA.html')
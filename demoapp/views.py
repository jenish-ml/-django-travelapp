from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import *
# Create your views here.
def index(request):
    places = Place.objects.all()
    users = Profile.objects.all()
    return render(request,"index.html",{'places':places,'users':users}) 

def about(request):
    places = Place.objects.all()
    users = Profile.objects.all()
    return render(request,'about.html',{'places':places,'users':users})

def contact(request):
    try:
        no1 = int(request.GET['No1'])
        no2 = int(request.GET['No2'])
        add = no1 + no2
        sub = no1 - no2
        mul = no1 * no2
        div = no1 / no2
        return render(request, 'contact.html', {'add': add, 'sub': sub, 'mul': mul, 'div': div})
    except:
        return render(request, 'contact.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass']
        repassword=request.POST['re_pass']
        if password==repassword:
            if User.objects.filter(username=name).exists():
                messages.info(request,"UserName already Exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Aready Exists')
                return redirect('register')
            User.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            print("User Created")
            return redirect('login')
        messages.info(request,'Password Not Matched')
    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def addplace(request):
    if request.method == 'POST':
        form = PlaceAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PlaceAddForm()

    return render(request, 'add_place.html', {'form': form})


def adduser(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserAddForm()
    return render(request,'add_user.html',{'form':form})
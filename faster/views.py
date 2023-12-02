from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def About(request):
    return render(request,'about.html')

def Base(request):
    return render(request,'base.html')

def Blog(request):
    return render(request,'our-blog/blog.html')

def Contact(request):
    return render(request,'contact.html')

def Home(request):
    return render(request,'home.html')

@login_required(login_url='/Account')
def Price(request):
    return render(request,'price.html')

def Service(request):
    return render(request,'service.html')

def Single(request):
    return render(request,'our-blog/single.html')

def Team(request):
    return render(request,'team.html')

def Account(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            user = f.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + user)
            return redirect('/')

    else:
        messages.success(request, 'Account was not successfully created')
        f = CustomUserCreationForm()
    return render(request,'account.html',{'form':f})

def Checkout(request):
    return render(request,'checkout.html')

def Thankyou(request):
    return render(request,'thankyou.html')


def loginU(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exists!') 
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in succesfully')
            return redirect('/')
        else:
            messages.error(request, 'Username or password does not exists')
            return redirect('/Account')
    
    
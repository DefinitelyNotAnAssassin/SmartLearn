from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from UserAuthentication.forms import LoginForm, UserForm

# Create your views here.


def login(request):
    items = { 
             
             'form': LoginForm(),
             
             }
    return render(request, "UserAuthentication/login.html", context = items)

def register(request):
    items = { 
             
             'form': UserForm(),
             
             }
    return render(request, "UserAuthentication/register.html", context = items)

def logout(request):
    logout_user(request)
    return redirect('index')    
   
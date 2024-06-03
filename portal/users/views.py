from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from users.forms import UserLogInForm, UserRegistrForm, UserUpdateForm, MarketPlaceCreateForm
from django.contrib import messages
from users.models import Employers, MyUser, MarketPlace
from django.contrib.auth import authenticate, login, logout


def marketplace(request):
    data = MarketPlace.objects.filter(employer_id=Employers.objects.get(user_id=request.user.id))
    context = {
        'data' : data,
        'title' : 'Marketplace'
    }
    return render(request, 'users/marketplace.html', context)

def marketplace_create(request):
    if request.method == 'POST':
        form = MarketPlaceCreateForm(data=request.POST)
        if form.is_valid():
            
            form.save(Employers.objects.get(user_id=request.user.id))
            return HttpResponseRedirect(reverse('index'))
    else:
        form = MarketPlaceCreateForm()
    context = {
        'form' : form,
        'title' : 'Create Marketplace'
        }
    return render(request, 'users/marketplacecreate.html', context)

def login_view(request):
    if request.method == 'POST':
        form = UserLogInForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # function "reverse()" get name urlpatern and namespace if it needs
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLogInForm()
    context = {
        'form' : form,
        'title' : 'Login'
        }
    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('users:login_view')


# Create your views here.
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserUpdateForm(instance=request.user)
    context = {
        'form' : form,
        'title' : 'Profile'
        }
    return render(request, 'users/profile.html', context)

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrForm()
    context = {
        'form' : form,
        'title' : 'Registration'
        }
    return render(request, 'users/register.html', context)
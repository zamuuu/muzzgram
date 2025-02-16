from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('feed') # If your are logged in, it sends it to the feed
    return render(request, 'users/home.html') # If its not just show the login or sign up page

def register(request):
    return render(request, 'users/register.html')
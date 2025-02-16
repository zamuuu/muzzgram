from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_user(request):
    if request.user.is_authenticated:
        return render(request, 'users/feed.html') # If your are logged in, it sends it to the feed
    else:
        if request.method == "POST": 
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('feed')
                # Redirect to a success page.
            else:
                messages.error(request, "Username or Password incorrect")
                return redirect('login')
                ...
        else:
            return render(request, 'users/home.html')

def register_user(request):
    return render(request, 'users/register.html')

@login_required
def feed(request):
    return render(request, "users/feed.html")
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import get_user_model

def home(request):
    if request.user.is_authenticated:
        return redirect('feed') # If your are logged in, it sends it to the feed
    return render(request, 'users/home.html') # If its not just show the login or sign up page

User = get_user_model()

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
        login(request, user)  
        return redirect("home")

    return render(request, "users/register.html")
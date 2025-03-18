from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import get_user_model

def home(request):
    if request.user.is_authenticated:
        return redirect('feed') # If your are logged in, it sends it to the feed
    return render(request, 'users/home.html') # If its not just show the login or sign up page


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

@login_required
def feed(request):
    return render(request, "users/feed.html")
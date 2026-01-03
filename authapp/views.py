from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 

# from django.core.mail import send_mail
# from restapi.settings import EMAIL_HOST_USER


# LOGIN VIEW
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# REGISTER VIEW
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = User.objects.create_user(username=username, password=password, email=email)
        return redirect('login')

    return render(request, 'register.html')


def dashboard_view(request):
    return render(request, "dashboard.html")


def forget_password(request):
    return render (request,  "forget_password.html")

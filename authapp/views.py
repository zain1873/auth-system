from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from django.contrib import messages
from django.core.mail import send_mail
import random
from django.utils import timezone
from django.db import models
import datetime
from .models import PasswordResetOTP

# -------------------------
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

# DASHBOARD
def dashboard_view(request):
    return render(request, "dashboard.html")

# FORGET PASSWORD (Send OTP)
def forget_password_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            otp = str(random.randint(100000, 999999))  # 6-digit OTP

            # Save OTP in DB
            PasswordResetOTP.objects.create(user=user, otp=otp)

            # Send OTP via email
            send_mail(
                subject="Your Password Reset OTP",
                message=f"Your OTP is {otp}. It is valid for 10 minutes.",
                from_email="your_email@example.com",
                recipient_list=[email],
            )

            # Store user ID in session
            request.session['reset_user_id'] = user.id
            messages.success(request, "OTP sent to your email!")
            return redirect('verify_otp_page')

        except User.DoesNotExist:
            messages.error(request, "Email not found!")
            return redirect('forget_password_page')

    return render(request, 'forget_password.html')

# -------------------------
# VERIFY OTP
def verify_otp_page(request):
    user_id = request.session.get('reset_user_id')
    if not user_id:
        messages.error(request, "Session expired. Start over.")
        return redirect('forget_password')

    if request.method == "POST":
        otp_input = request.POST.get('otp')
        try:
            otp_obj = PasswordResetOTP.objects.filter(user_id=user_id, otp=otp_input).last()
            if otp_obj and not otp_obj.is_expired():
                request.session['otp_verified'] = True
                messages.success(request, "OTP verified! You can reset your password now.")
                return redirect('reset_password_page')
            else:
                messages.error(request, "Invalid or expired OTP!")
        except PasswordResetOTP.DoesNotExist:
            messages.error(request, "Invalid OTP!")

    return render(request, 'verify_otp.html')

# -------------------------
# RESET PASSWORD
def reset_password_page(request):
    user_id = request.session.get('reset_user_id')
    otp_verified = request.session.get('otp_verified', False)

    if not user_id or not otp_verified:
        messages.error(request, "Unauthorized access!")
        return redirect('forget_password_page')

    if request.method == "POST":
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.get(id=user_id)
            user.set_password(password)
            user.save()

            # Clear session
            request.session.pop('reset_user_id')
            request.session.pop('otp_verified')

            messages.success(request, "Password reset successfully!")
            return redirect('login')
        else:
            messages.error(request, "Passwords do not match!")

    return render(request, 'reset_password.html')

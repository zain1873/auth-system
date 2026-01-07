# authapp/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class PasswordResetOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6) 
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        # OTP valid for 10 minutes
        return timezone.now() > self.created_at + datetime.timedelta(minutes=10)

    def __str__(self):
        return f"{self.user.email} - {self.otp}"



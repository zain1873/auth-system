# models.py
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta

def token_expiry_time():
    return now() + timedelta(hours=1)

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=token_expiry_time)

    def __str__(self):
        return self.user.email

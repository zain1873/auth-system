from django.urls import path
from .views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('api/password-reset/', PasswordResetView.as_view(), name='api-password-reset'),
    path('api/password-reset-confirm/', PasswordResetConfirmView.as_view(), name='api-password-reset-confirm'),
]
    
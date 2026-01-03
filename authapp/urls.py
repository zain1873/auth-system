from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, register_view, dashboard_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("login-page/", login_view, name="login"),
    path("register-page/", register_view, name="register"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset_form.html'
    ), name='password_reset')


]

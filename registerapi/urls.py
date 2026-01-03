from django.urls import path
from .views import register_view

urlpatterns = [
    path('', register_view.as_view(), name='api-register'),  
]

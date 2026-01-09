# admin.py
from django.contrib import admin
from django.contrib.auth.models import User

from bookings.models import TableBooking



admin.site.unregister(User) 
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active') 




# booking app model
admin.site.register(TableBooking)
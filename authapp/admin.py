# admin.py
from django.contrib import admin
from django.contrib.auth.models import User

from bookings.models import TableBooking
from contact.models import Contact



admin.site.unregister(User) 
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active') 




#coffee booking app model
admin.site.register(TableBooking)

# coffee contact app model
admin.site.register(Contact)

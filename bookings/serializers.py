from rest_framework import serializers
from .models import TableBooking

class TableBookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = TableBooking
        fields = ['id', 'user', 'date', 'time', 'persons', 'created_at']
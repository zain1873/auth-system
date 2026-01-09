from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .models import TableBooking
from serializers import TableBookingSerializer
from rest_framework.response import Response


# Create your views here.

class TableBookingView(APIView):
  def get(slef, request):
    bookings = TableBooking.objects.all()
    serializer = TableBookingSerializer(bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

    
  def post(slef, request):
    serializer = TableBookingSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from django.urls import path
from .views import TableBookingView

urlpatterns = [
  path("table-booking/", TableBookingView.as_view(), name="table-book")
]

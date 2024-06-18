from django.shortcuts import render
from django.views import generic
from .models import *
# from .models import Booking


# Create your views here.
def home(request):
    return render(request, "index.html")

def booking(request):
    return render(request, "booking/booking.html")

def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    
    return render(request, "booking/booking_list.html")

# class BookingList(generic.ListView):
#     queryset = Booking.objects.filter()
#     template_name = "booking_list.html"





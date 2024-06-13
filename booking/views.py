from django.shortcuts import render
from django.views import generic
from .models import Booking
#from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "index.html")

def booking(request):
    return render(request, "booking/booking.html")

def my_bookings(request):
    return render(request, "booking/my_bookings.html")

class BookingList(generic.ListView):
    queryset = Booking.objects.all()
    template_name = "booking_list.html"





from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request, "index.html")

def booking(request):
    return render(request, "booking/booking.html")

def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    
    return render(
        request, 
        "booking/booking_list.html",
        {
            'bookings':bookings
        },
    )

# def edit_booking(request)

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
    return redirect('my_bookings')







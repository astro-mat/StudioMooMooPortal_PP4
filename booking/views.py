from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request, "index.html")

def booking(request):
    return render(request, "booking/booking.html")

def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    booking_form = BookingForm()
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
    
    return render(
        request, 
        "booking/booking_list.html",
        {
            'booking_form' : booking_form,
            'bookings': bookings,
        },
    )


def edit_booking(request, booking_id):
    # view to edit booking
    queryset = Booking.objects.all()
    booking = get_object_or_404(queryset, pk=booking_id)
    booking_form = BookingForm(instance=booking)

    if request.method == "POST":
        queryset = Booking.objects.all()
        booking = get_object_or_404(queryset, pk=booking_id)
        booking_form = BookingForm(data=request.POST, instance=booking)

        if booking_form.is_valid():
            booking = booking_form.save()
            messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
            return HttpResponseRedirect(reverse('my_bookings'))
        else:
            messages.add_message(request, messages.ERROR, 'Error updating booking!')
    return render(
        request, 
        "booking/booking_edit.html",
        {
            'booking_form' : booking_form,
        },
    )
        
    

# def delete_booking(request, booking_id):
#     # View to delete booking
#     booking = get_object_or_404(Booking, id=booking_id, user=request.user)
#     if request.method == 'POST':
#         booking.delete()
#     return redirect('booking/my_booking')

def delete_booking(request, booking_id):
    """
    view to delete comment
    """
    booking = get_object_or_404(Booking, pk=booking_id)
    
    if request.method == 'POST':
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Booking Deleted!')
        return HttpResponseRedirect(reverse('my_bookings'))
    else:
        return render(
        request, 
        "booking/booking_delete.html",
        {
            'booking' : booking,
        },
    )

    
def success_booking(request, booking_id):
    """
    Success page after making a booking
    """
    booking = get_object_or_404(Booking, pk=booking_id)
    
    if request.method == 'POST':
        messages.add_message(request, messages.SUCCESS, 'Booking created!')
        return HttpResponseRedirect(reverse('my_bookings'))
    else:
        return render(
        request, 
        "booking/booking_success.html",
        {
            'booking' : booking,
        },
    )




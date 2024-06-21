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
    booking_form = BookingForm()
    
    return render(
        request, 
        "booking/booking_list.html",
        {
            'bookings': bookings,
            'booking_form' : booking_form,
        },
    )

# def edit_booking(request)
def edit_booking(request, slug, booking_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        booking = get_object_or_404(Comment, pk=booking_id)
        booking_form = BookingForm(data=request.POST, instance=comment)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.post = post
            booking.approved = False
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating booking!')

    return HttpResponseRedirect(reverse('booking_detail', args=[slug]))

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
    return redirect('booking/booking_detail')







from django.shortcuts import render
from django.views import generic
from .models import Booking
#from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "index.html")

def booking(request):
    return render(request, "booking.html")



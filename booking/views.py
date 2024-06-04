from django.shortcuts import render, HttpResponse
#from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def home(request):
    return render(request, "booking.html")
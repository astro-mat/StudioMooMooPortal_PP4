from django.urls import path
from . import views
# from .forms import BookingForm

urlpatterns = [
    path("", views.home, name="home"),
    path("booking/", views.booking, name="booking"),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    # path('my_bookings/', views.BookingList.as_view(), name='my_bookings'),
]


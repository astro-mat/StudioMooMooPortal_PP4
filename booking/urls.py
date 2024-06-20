from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("booking/", views.booking, name="booking"),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('<slug:slug>/delete_booking/<int:booking_id>',views.delete_booking, name='delete_booking'),
]


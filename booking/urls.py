from django.urls import path
from . import views

app_name = 'booking'
urlpatterns = [
    path("", views.home, name='home'),
    path("booking/", views.booking, name='booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('edit_booking/<int:booking_id>',
         views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:booking_id>',
         views.delete_booking, name='delete_booking'),
    path('success_booking/<int:booking_id>',
         views.success_booking, name='success_booking'),
]

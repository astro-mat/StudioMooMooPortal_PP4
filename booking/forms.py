from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('Artist_Name','start_time','end_time','BookingRequirements')
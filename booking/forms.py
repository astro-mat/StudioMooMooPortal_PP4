from .models import Booking
from django import forms

        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('Artist_Name','Date','Booking_Requirements')
        widgets = {
            'Artist_Name': forms.Textarea(attrs={'cols': 60, 'rows': 1}),
            'Date': forms.TextInput(attrs={'type': 'date'}),
            'Booking_Requirements': forms.Textarea()
        }
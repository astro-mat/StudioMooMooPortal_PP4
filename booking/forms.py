from .models import Booking
from django import forms

        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('artist_name','date','booking_requirements')
        widgets = {
            'nrtist_name': forms.Textarea(attrs={'cols': 60, 'rows': 1}),
            'date': forms.TextInput(attrs={'type': 'date'}),
            'booking_requirements': forms.Textarea()
        }
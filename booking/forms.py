from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from datetime import datetime, date
from .models import Booking

        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('artist_name','date','booking_requirements')
        widgets = {
            'artist_name': forms.Textarea(attrs={'cols': 60, 'rows': 1}),
            'date': DateInput(attrs={'type': 'date'}),
            'booking_requirements': forms.Textarea()
        }

    def clean(self):
            """
            Custom validation to ensure date and time are valid and available
            """
            cleaned_data = super().clean()
            date = cleaned_data.get("date")

            if date < date.today():
                raise ValidationError("Please select a date in the future.")

            existing_bookings = Booking.objects.filter(date=date).exclude(id=self.instance.id)
            print('existing_bookings', existing_bookings)

            if existing_bookings:
                raise ValidationError(
                    "That date is already taken, "
                    "please select a different date."
                )
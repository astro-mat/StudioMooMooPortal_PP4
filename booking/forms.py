from .models import Booking
from django import forms

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ('Artist_Name','Date','start_time','end_time','Booking_Requirements')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('Artist_Name','Date','start_time','end_time','Booking_Requirements')
        widgets = {
            'Artist_Name': forms.Textarea(attrs={'cols': 60, 'rows': 1}),
            'Date': forms.TextInput(attrs={'type': 'date'}),
            'start_time': forms.TextInput(attrs={'type': 'time'}),
            'end_time': forms.TextInput(attrs={'type': 'time'}),
            'Booking_Requirements': forms.Textarea()
        }
        
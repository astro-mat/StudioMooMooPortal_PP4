from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('Artist_Name','start_time','end_time','BookingRequirements')
        # Artist_Name = forms.CharField()
        # start_time = forms.DateTimeField()
        # end_time = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
        # BookingRequirements = forms.CharField()
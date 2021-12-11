from django import forms
from .models import Booking



class ReservationForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'party_size',
            'date',
            'time',
        ]
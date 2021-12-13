from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ("name",)
        date = forms.DateField(widget=forms.TextInput(
            attrs={'type': 'date'}), required=True
            )
        fields = (
            'party_size',
            'date',
            'time',
        )            
        widgets = {
            'date': DateInput(),
        }
        

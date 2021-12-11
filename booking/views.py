from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking
from .forms import ReservationForm


# Create your views here.


def index(request):
    # redirect to index view
    return render(
        request,
        'index.html',
        {
            "booking_form": ReservationForm()
        }
        )



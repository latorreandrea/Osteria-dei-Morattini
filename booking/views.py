from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking
from .forms import ReservationForm


# Create your views here.


def index(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = ReservationForm()
    return render(request, 'index.html', {'booking_form': form})

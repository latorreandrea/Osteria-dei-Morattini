from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking
from .forms import ReservationForm


# Create your views here.


def index(request):
    user = request.user
    user_id = get_object_or_404(User, username=user)
    
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.instance.name = user_id
            form.save()
            return render(request, 'index.html', {'booking_form': form})
    else:
        form = ReservationForm()
    return render(request, 'index.html', {'booking_form': form})

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Booking
from .forms import ReservationForm
from django.contrib import messages


# Create your views here.


def index(request):
      
    if request.method == "POST":
        user = request.user
        user_id = get_object_or_404(User, username=user)
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.instance.name = user_id
            form.save()
            messages.success(request, 'Your reservation has been taken!')
            return redirect('reservations')
    else:
        form = ReservationForm()
        messages.error(request, 'Invalid form submission.')
        messages.error(request, form.errors)
        return render(request, 'index.html', {'booking_form': form})


def user_reservation(request):
    user = request.user
    user_id = get_object_or_404(User, username=user)
    bookings = Booking.objects.filter(name=user_id)
    
    return render(request, 'reservations.html', {'user_booking_list': bookings})


def edit_reservation(request, bookings_id):
    
    this_booking = get_object_or_404(Booking, id=bookings_id)
    
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=this_booking)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation has been taken!')
            return redirect('reservations')
        else:
            print(form.errors)
    else:
        form = ReservationForm(instance=this_booking)
        messages.error(request, 'Invalid form submission.')
        messages.error(request, form.errors)
           
    
    return render(request, 'edit_reservation.html', {'booking_form': form})

def delete_reservation(request, bookings_id):    
    this_booking = get_object_or_404(Booking, id=bookings_id)
    this_booking.delete()
    return redirect('reservations')


def menu(request):
    return render(request, 'menu.html',)

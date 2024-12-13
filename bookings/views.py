from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm

# Create your views here.
def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        total_price = request.POST.get('total_price')
        if form.is_valid():
            booking = form.save(commit=False)
            booking.owner = request.user
            booking.total_price = total_price
            booking.save()
            return redirect('home')
    else:
        form = BookingForm()
        context = {
            "form": form,
        }
        return render(request, 'bookings/create_booking.html', context)


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        total_price = request.POST.get('total_price')
        if form.is_valid():
            booking = form.save(commit=False)
            booking.owner = request.user
            booking.total_price = total_price
            booking.save()
            return redirect('home')
    else:
        form = BookingForm(instance=booking)
        context = {
            "form": form,
            "total_price": booking.total_price,
        }
        return render(request, 'bookings/edit_booking.html', context)
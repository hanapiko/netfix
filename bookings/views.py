from django.shortcuts import redirect, render

from django.shortcuts import render
from django.urls import reverse
from bookings.models import Bookings

from service.models import Service
from .forms import BookingForm

def booking_view(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.method == 'POST':
        booking = Bookings(service=service, user=request.user)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user 
            booking.price = service.price_per_hour * int(request.POST['hours'])
            print(booking.price)
            booking.save()
            return redirect(reverse('profile'))
    else:
        form = BookingForm(instance=Bookings(service=service))
    return render(request, 'book_service.html', {'form': form, 'service': service})

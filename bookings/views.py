from django.shortcuts import redirect, render
from django.urls import reverse
from bookings.models import Bookings
from service.models import Service
from .forms import BookingForm

# View to handle booking a specific service
def booking_view(request, service_id):
    # Retrieve the service being booked by its ID
    service = Service.objects.get(id=service_id)

    if request.method == 'POST':
        # Create a booking object and pre-fill it with the current user and selected service
        booking = Bookings(service=service, user=request.user)
        
        # Bind submitted form data to the BookingForm, using the pre-filled booking instance
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            # Do not save to the database yet to allow manual adjustments
            booking = form.save(commit=False)

            # Assign the logged-in user (redundant here but still ensures accuracy)
            booking.user = request.user

            # Calculate the booking price: service price per hour * number of hours submitted
            booking.price = service.price_per_hour * int(request.POST['hours'])
            
            # Optional: Print the calculated price to the console (useful for debugging)
            print(booking.price)

            # Save the booking to the database
            booking.save()

            # Redirect the user to the profile page after successful booking
            return redirect(reverse('profile'))
    else:
        # If it's a GET request, display an empty form pre-filled with the selected service
        form = BookingForm(instance=Bookings(service=service))

    # Render the booking form page with the form and service context
    return render(request, 'book_service.html', {'form': form, 'service': service})

from django.db import models
from django.forms import ValidationError
from main.models import AppUser
from services.models import Service
from datetime import datetime

# Model representing a booking made by a user for a specific service
class Bookings(models.Model):
    # Foreign key linking to the Service being booked
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    
    # Foreign key linking to the user making the booking
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    
    # Address where the service will be provided
    address = models.TextField(max_length=300, null=False)
    
    # Date and time when the booking was made
    booking_date = models.DateTimeField(default=datetime.now, null=False)
    
    # Total price for the booking, expected to be service.price_per_hour * hours
    price = models.DecimalField(max_digits=100, decimal_places=2)  # Consider reducing max_digits to a more reasonable value

    def __str__(self):
        # Defines how the booking will be displayed, especially in Django admin or lists
        # Displays service name, service field, price, and booking date
        return f"{self.service.name} - {self.service.field} - {self.price} - {self.booking_date}"

    def clean(self):
        """
        Model-level validation to ensure:
        - Only users with the 'CUSTOMER' role can make bookings
        - The address is not empty or just whitespace
        """
        if self.user.field_of_work != 'CUSTOMER':
            raise ValidationError('Only customers can book services')

        # Remove leading and trailing whitespace from the address
        self.address = self.address.strip()

        # Check if address is now empty after trimming
        if not self.address:
            raise ValidationError('Address is required')

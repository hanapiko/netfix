from django import forms
from bookings.models import Bookings

# Form class for creating and updating Booking instances
class BookingForm(forms.ModelForm):
    # Custom form field to capture the number of hours, must be at least 1
    hours = forms.IntegerField(min_value=1)

    class Meta:
        # The form is based on the Bookings model
        model = Bookings
        # Only the 'address' and the custom 'hours' fields will be displayed in the form
        fields = ['address', 'hours']

    def __init__(self, *args, **kwargs):
        # Call the parent constructor to initialize the form
        super().__init__(*args, **kwargs)
        # Add the 'autofocus' HTML attribute to the 'address' field's input widget
        self.fields['address'].widget.attrs.update({'autofocus': 'autofocus'})

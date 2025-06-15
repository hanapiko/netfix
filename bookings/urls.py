from django.urls import path
from . import views

# URL patterns for the bookings app
urlpatterns = [
    # URL for booking a specific service
    # Expects an integer 'service_id' as part of the URL
    # This URL is mapped to the 'booking_view' function in views.py
    # Named URL pattern: 'book_service'
    path('book_service/<int:service_id>/', views.booking_view, name='book_service'),
]

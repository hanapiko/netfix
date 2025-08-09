from django.contrib import admin
from .models import Bookings

@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ['service', 'user', 'price', 'booking_date', 'address']
    list_filter = ['booking_date', 'service__field']
    search_fields = ['user__username', 'service__name', 'address']
    readonly_fields = ['booking_date']

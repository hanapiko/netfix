from django.apps import AppConfig

# Configuration class for the 'bookings' app
class BookingsConfig(AppConfig):
    # Specifies the default type of primary key field to use for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # The name of the app this configuration applies to
    name = 'bookings'

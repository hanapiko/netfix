import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    # This marks this migration as the initial migration for the app.
    initial = True

    # Dependencies define which migrations need to run before this one.
    dependencies = [
        # Depends on the initial migration of the 'service' app.
        ('service', '0001_initial'),
        # Depends on the user model, allowing for custom user models.
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    # Operations to apply for this migration.
    operations = [
        # This creates the 'Bookings' table in the database.
        migrations.CreateModel(
            name='Bookings',
            fields=[
                # Primary key field (auto-incrementing).
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                
                # Field to store the booking address, max length 300 characters.
                ('address', models.TextField(max_length=300)),
                
                # Field to store the date and time of the booking.
                # Defaults to the current datetime when the record is created.
                ('booking_date', models.DateTimeField(default=datetime.datetime.now)),
                
                # Field to store the price of the booking.
                # Maximum of 8 digits, with 2 digits after the decimal point.
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                
                # Foreign key linking each booking to a service.
                # If the linked service is deleted, the booking will also be deleted (CASCADE).
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.service')),
                
                # Foreign key linking each booking to a user.
                # If the linked user is deleted, the booking will also be deleted (CASCADE).
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

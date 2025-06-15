# This is an auto-generated Django migration file.

from django.db import migrations, models

class Migration(migrations.Migration):
    # This section defines the migration dependencies.
    # It indicates that this migration depends on the initial migration (0001_initial) of the 'bookings' app.
    dependencies = [
        ('bookings', '0001_initial'),
    ]

    # This section lists the operations to be applied in this migration.
    operations = [
        # This operation alters the 'price' field of the 'bookings' model.
        # The new field type is DecimalField with up to 100 total digits and 2 decimal places.
        migrations.AlterField(
            model_name='bookings',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]

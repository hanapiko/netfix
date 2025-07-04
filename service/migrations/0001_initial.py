# Generated by Django 4.2.8 on 2025-06-22 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=500)),
                ('field', models.CharField(choices=[('AIR_CONDITIONER', 'Air Conditioner'), ('CARPENTRY', 'Carpentry'), ('ELECTRICITY', 'Electricity'), ('GARDENING', 'Gardening'), ('HOME_MACHINES', 'Home Machines'), ('HOUSEKEEPING', 'Housekeeping'), ('INTERIOR_DESIGN', 'Interior Design'), ('LOCKS', 'Locks'), ('PAINTING', 'Painting'), ('PLUMBING', 'Plumbing'), ('WATER_HEATERS', 'Water Heaters')], max_length=50)),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('company_username', models.ForeignKey(limit_choices_to={'field_of_work__ne': 'CUSTOMER'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]

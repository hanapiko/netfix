# Generated by Django 5.2.3 on 2025-06-22 06:51

import django.contrib.auth.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=254, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('field_of_work', models.CharField(choices=[('CUSTOMER', 'Customer'), ('AIR_CONDITIONER', 'Air Conditioner'), ('ALL_IN_ONE', 'All in One'), ('CARPENTRY', 'Carpentry'), ('ELECTRICITY', 'Electricity'), ('GARDENING', 'Gardening'), ('HOME_MACHINES', 'Home Machines'), ('HOUSEKEEPING', 'Housekeeping'), ('INTERIOR_DESIGN', 'Interior Design'), ('LOCKS', 'Locks'), ('PAINTING', 'Painting'), ('PLUMBING', 'Plumbing'), ('WATER_HEATERS', 'Water Heaters')], default='CUSTOMER', max_length=50)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

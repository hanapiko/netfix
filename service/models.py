from django.db import models
from django.db.models import Q
from main.models import ACTIVITY_CHOICES, AppUser


class Service(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=500)
    field = models.CharField(
        max_length=50,
        choices=[
            (x, y) for x, y in ACTIVITY_CHOICES if x not in ['ALL_IN_ONE', 'CUSTOMER']
        ]
    )
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)  # Changed from 100 to 10
    created_date = models.DateTimeField(auto_now_add=True)
    company_username = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        to_field='username',
        limit_choices_to=~Q(field_of_work='CUSTOMER')  # Using Q object for proper negation
    )

    def __str__(self):
        return self.name

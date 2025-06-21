from django.db import models

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
    price_per_hour = models.DecimalField(max_digits=100, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    company_username = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, to_field='username', limit_choices_to={'field_of_work__ne': 'CUSTOMER'})

    def __str__(self):
        return self.name
